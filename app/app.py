from flask import Flask, render_template, request, Response, url_for
from ultralytics import YOLO
import os, cv2, time, pathlib

# --------- SETTINGS ---------
MODEL_PATH = r"C:\Users\OWNER\runs\detect\train16\weights\best.pt"  # ✅ your trained model path
CONF = 0.30
IOU = 0.6
MAX_DET = 20  # max detections per image
IMG_SIZE = 640
CAM_INDEX = 0  # Try 1 or 2 if webcam doesn't open
# ----------------------------

BASE_DIR = pathlib.Path(__file__).resolve().parents[1]
UPLOAD_DIR = BASE_DIR / "app" / "static" / "uploads"
RESULT_DIR = BASE_DIR / "app" / "static" / "results"
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
RESULT_DIR.mkdir(parents=True, exist_ok=True)

app = Flask(__name__)

# ✅ Load YOLO model
if os.path.exists(MODEL_PATH):
    print(f"[INFO] Loaded model from: {MODEL_PATH}")
    model = YOLO(MODEL_PATH)
else:
    print("[ERROR] Model path not found. Check MODEL_PATH.")
    raise SystemExit(1)


# ---------- ROUTES ----------
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():
    if "file" not in request.files or request.files["file"].filename == "":
        return "❌ No file uploaded", 400

    f = request.files["file"]
    in_path = UPLOAD_DIR / f.filename
    f.save(in_path)

    # ✅ Create a unique folder for each run
    unique_run = f"pred_{int(time.time())}"

    # Run detection
    results = model.predict(
        source=str(in_path),
        conf=CONF,
        iou=IOU,
        max_det=MAX_DET,
        imgsz=IMG_SIZE,
        save=True,
        project=str(RESULT_DIR),
        name=unique_run,
        exist_ok=False
    )

    # ✅ Find output image
    out_dir = RESULT_DIR / unique_run
    candidates = [p for p in out_dir.glob("*") if p.suffix.lower() in [".jpg", ".png", ".jpeg"]]
    if not candidates:
        return "❌ No result image generated", 500
    out_img = candidates[0]

    # ✅ Count detections
    dets = results[0].boxes if results else []
    num = len(dets) if dets is not None else 0

    # ✅ Add cache-busting
    cache = f"?t={int(time.time())}"
    result_url = url_for("static", filename=f"results/{unique_run}/{out_img.name}") + cache

    return render_template("result.html", result_image=result_url, num_detections=num)


# ---------- LIVE CAMERA ----------
def gen_frames():
    cap = cv2.VideoCapture(CAM_INDEX)
    if not cap.isOpened():
        print("[ERROR] Could not open webcam.")
        return
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # 🔎 Run YOLO detection
            res = model.predict(
                source=frame,
                conf=CONF,
                iou=IOU,
                max_det=MAX_DET,
                imgsz=IMG_SIZE,
                stream=False,
                verbose=False
            )

            # 🧮 Count detections
            dets = res[0].boxes if res else []
            num_potholes = len(dets) if dets is not None else 0

            # 📊 Draw boxes
            annotated = res[0].plot()

            # 🟢 or 🔴 Overlay detection status
            if num_potholes > 0:
                text = f"Potholes detected: {num_potholes}"
                color = (0, 255, 0)  # green
            else:
                text = "No potholes detected 🚫"
                color = (0, 0, 255)  # red

            cv2.putText(
                annotated,
                text,
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1.2,
                color,
                3,
                cv2.LINE_AA
            )

            # 📤 Stream frame
            ok, buffer = cv2.imencode(".jpg", annotated)
            if not ok:
                continue
            yield (b"--frame\r\nContent-Type: image/jpeg\r\n\r\n" + buffer.tobytes() + b"\r\n")
    finally:
        cap.release()


@app.route("/camera")
def camera():
    return render_template("camera.html")


@app.route("/video_feed")
def video_feed():
    return Response(gen_frames(), mimetype="multipart/x-mixed-replace; boundary=frame")


# ---------- MAIN ----------
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False, threaded=True)