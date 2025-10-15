import os
import json
import time
import base64
import pathlib
import cv2
import requests

# -------- load config --------
CFG_PATH = pathlib.Path(__file__).with_name("config.json")
if not CFG_PATH.exists():
    raise SystemExit("Missing config.json next to this script.")
cfg = json.loads(CFG_PATH.read_text())
LAMBDA_URL = cfg["LAMBDA_URL"].strip()
API_KEY    = cfg["API_KEY"].strip()

def send_to_lambda(path: str):
    with open(path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode("utf-8")
    r = requests.post(
        LAMBDA_URL,
        headers={"x-api-key": API_KEY, "Content-Type": "application/json"},
        json={"image_b64": b64},
        timeout=30,
    )
    r.raise_for_status()
    return r.json()

def try_open(idx: int, backend=None):
    if backend is None:
        cap = cv2.VideoCapture(idx)
    else:
        cap = cv2.VideoCapture(idx, backend)
    time.sleep(0.2)
    if cap.isOpened():
        ok, _ = cap.read()
        if ok:
            return cap
    cap.release()
    return None

def open_first_camera(max_idx=6):
    # On Windows, DSHOW and MSMF backends are the usual suspects
    backends = []
    if hasattr(cv2, "CAP_DSHOW"): backends.append(cv2.CAP_DSHOW)
    if hasattr(cv2, "CAP_MSMF"):  backends.append(cv2.CAP_MSMF)
    backends.append(None)  # default backend as last resort

    # Try index 0 first (most common), then 1..max_idx-1
    for idx in list(range(0, max_idx)):
        for be in backends:
            cap = try_open(idx, be)
            if cap:
                return cap, idx, be
    return None, None, None

def file_fallback():
    # simple text prompt fallback (no GUI dependencies)
    p = input("No camera found. Enter a PNG/JPG path to OCR (or press Enter to quit): ").strip()
    if not p:
        return None
    if not pathlib.Path(p).exists():
        print("File not found.")
        return None
    return p

def main():
    # ---- try camera ----
    cap, idx, be = open_first_camera()
    if not cap:
        print("⚠️  Could not access any camera.")
        # fallback: test with a local file (like your working test_image.py)
        p = file_fallback()
        if not p: return
        print("➡️  Sending to Lambda…")
        try:
            data = send_to_lambda(p)
            print("✅ OCR lines:")
            for ln in data.get("lines", []):
                print(ln)
        except Exception as e:
            print("❌ OCR failed:", e)
        return

    be_name = {getattr(cv2, "CAP_DSHOW", -1): "CAP_DSHOW",
               getattr(cv2, "CAP_MSMF", -2): "CAP_MSMF"}.get(be, "default")
    print(f"📷 Using camera index {idx} via {be_name}")
    print("Press SPACE to capture, or 'q' to quit.")

    while True:
        ok, frame = cap.read()
        if not ok:
            continue
        cv2.imshow("Camera", frame)
        k = cv2.waitKey(1) & 0xFF

        if k == ord(' '):
            out = "capture.png"
            cv2.imwrite(out, frame)
            print(f"💾 Saved {out}")
            print("➡️  Sending to Lambda…")
            try:
                data = send_to_lambda(out)
                print("✅ OCR lines:")
                for ln in data.get("lines", []):
                    print(ln)
            except Exception as e:
                print("❌ OCR failed:", e)
            break
        elif k in (ord('q'), 27):
            print("👋 Quit without capturing.")
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
