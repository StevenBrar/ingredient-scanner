# lambda_function.py
import os
import json
import base64
import boto3

# 1) Set this in Lambda → Configuration → Environment variables (Key: API_KEY)
API_KEY = os.getenv("API_KEY")

# 2) Textract client (region comes from the Lambda environment automatically)
textract = boto3.client("textract")

def handler(event, context):
    """
    Expects:
      - Header: x-api-key = <your secret> (must match API_KEY env var)
      - Body: either a raw base64 image string OR JSON: {"image_b64":"..."}
    Returns:
      {"lines": ["line1", "line2", ...]}
    """

    # --- CORS preflight (if called from a browser) ---
    if event.get("requestContext", {}).get("http", {}).get("method") == "OPTIONS":
        return _resp(204, {})

    # --- Auth check (simple shared secret in header) ---
    headers = event.get("headers") or {}
    supplied_key = None
    for k, v in headers.items():
        if k.lower() == "x-api-key":
            supplied_key = v
            break

    if API_KEY and supplied_key != API_KEY:
        return _resp(401, {"error": "unauthorized"})

    # --- Parse body (raw base64 OR {"image_b64": "..."} ) ---
    body = event.get("body") or ""
    if event.get("isBase64Encoded"):
        # Function URLs may mark body as base64-encoded string
        body = base64.b64decode(body).decode("utf-8")

    if body.strip().startswith("{"):
        try:
            image_b64 = json.loads(body).get("image_b64", "")
        except Exception:
            return _resp(400, {"error": "invalid JSON body"})
    else:
        image_b64 = body

    if not image_b64:
        return _resp(400, {"error": "missing image_b64"})

    # --- Call Textract ---
    try:
        img_bytes = base64.b64decode(image_b64)
    except Exception:
        return _resp(400, {"error": "image_b64 is not valid base64"})

    try:
        resp = textract.detect_document_text(Document={"Bytes": img_bytes})
        lines = [
            b["Text"] for b in resp.get("Blocks", [])
            if b.get("BlockType") == "LINE" and b.get("Text")
        ]
        return _resp(200, {"lines": lines})
    except Exception as e:
        # surface any textract/permission errors
        return _resp(500, {"error": str(e)})

def _resp(status_code: int, data: dict):
    """Uniform response with CORS headers."""
    return {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "application/json",
            # CORS (keep in sync with Function URL CORS settings)
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "*",
            "Access-Control-Allow-Methods": "POST, OPTIONS",
        },
        "body": json.dumps(data),
    }

# Shim so the default Lambda handler setting "lambda_function.lambda_handler" works:
def lambda_handler(event, context):
    return handler(event, context)
