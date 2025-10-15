import os, json, pathlib, base64, requests, sys

# load config
cfg_path = pathlib.Path(__file__).with_name("config.json")
cfg = json.loads(cfg_path.read_text())
URL = cfg["LAMBDA_URL"].strip()
KEY = cfg["API_KEY"].strip()

# pick the file: "image1", "image1.png", "image1.jpg", "image1.jpeg"
candidates = ["image1", "image1.png", "image1.jpg", "image1.jpeg"]
if len(sys.argv) > 1:
    candidates = [sys.argv[1]] + candidates

img_path = next((c for c in candidates if pathlib.Path(c).exists()), None)
if not img_path:
    raise SystemExit(f"Couldn't find any of: {', '.join(candidates)} in this folder.")

with open(img_path, "rb") as f:
    img64 = base64.b64encode(f.read()).decode("utf-8")

r = requests.post(
    URL,
    headers={"x-api-key": KEY, "Content-Type": "application/json"},
    json={"image_b64": img64},
    timeout=30,
)
print("Status:", r.status_code)
print("Response:", r.text)

# Pretty-print lines if present
try:
    data = r.json()
    if "lines" in data:
        print("\nOCR lines:")
        for ln in data["lines"]:
            print(ln)
except Exception:
    pass
