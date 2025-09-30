🛞 Pothole Detection System 🚧 | YOLOv8 + Flask + Computer Vision

A real-time web application that detects potholes from road images or live camera feed using YOLOv8 (You Only Look Once) deep learning model and a Flask backend.
This project helps improve road safety, infrastructure monitoring, and autonomous vehicle navigation by automatically identifying damaged road surfaces.

⸻

📸 Demo Preview

🚀 Real-time detection:
	•	✅ Detects potholes from uploaded road images
	•	📹 Live detection from webcam feed
	•	🟢 Displays number of potholes detected (with confidence)
	•	🛑 Shows No potholes detected 🚫 clearly when none are found

⸻

🧠 Features

✨ Core Features:
	•	🧠 Real-time pothole detection using YOLOv8 deep learning model
	•	📷 Support for both image upload and live camera feed
	•	📊 Automatic counting of detected potholes
	•	🚫 Smart filtering to remove false detections (e.g., shadows, cracks)
	•	🔊 Custom detection confidence, IoU, and box limits
	•	💻 Flask-powered backend with responsive HTML/CSS/JS frontend

⸻

🏗 Project Structure
```bash
potholes_detection_project/
│
├── app/
│   ├── templates/
│   │   ├── index.html        # Homepage upload interface
│   │   ├── result.html       # Detection result page
│   │   └── camera.html       # Live detection page
│   ├── static/
│   │   ├── uploads/          # Uploaded images
│   │   └── results/          # Detection output images
│
├── data/                     # Dataset (images + labels)
│   ├── images/
│   └── labels/
│
├── models/                   # Trained YOLO models (.pt)
├── app.py                    # Main Flask backend
├── requirements.txt          # Python dependencies
└── README.md                 # 📄 This file
```
---

## ⚙ Tech Stack

| Tool / Library         | Purpose                              |
|------------------------|--------------------------------------|
| 🐍 Python 3.10+       | Programming language                |
| 🚀 Flask             | Web backend framework              |
| 🤖 YOLOv8 (Ultralytics)| Object detection model              |
| 📷 OpenCV             | Image processing + webcam access   |
| 🧠 PyTorch           | Deep learning backend              |
| 🧪 HTML/CSS/JS       | Frontend UI                        |

---

## 🧰 Installation & Setup

Follow these steps to set up and run the pothole detection project on your local machine:

1️⃣ Clone the repository:  
git clone https://github.com/emmanoel24/pothole-detection.git  
cd pothole-detection

2️⃣ Create and activate a virtual environment:  
python -m venv venv  

- On Windows:  
venv\Scripts\activate  

- On Mac/Linux:  
source venv/bin/activate

3️⃣ Install dependencies:  
pip install -r requirements.txt

4️⃣ Run the Flask application:  
python app.py

✅ The application will start locally. Open your browser and go to:  
http://127.0.0.1:5000

💡 Tip: If you encounter missing package errors, install them manually:  
pip install ultralytics flask opencv-python torch torchvision

📂 Dataset

The YOLOv8 model was trained on a custom pothole dataset consisting of:
	•	🛣 100+ labeled road images (with and without potholes)
	•	📏 Images annotated using Makesense.ai
	•	🧪 Negative examples (clean roads) for better accuracy

To train your own model:
```bash
yolo detect train model=yolov8s.pt data=data/data.yaml epochs=100 imgsz=640
```
## 📊 Results & Performance

The pothole detection model was trained on a custom dataset and achieved strong detection performance. Below are the key evaluation metrics:

| Metric              | Value         |
|---------------------|---------------|
| ✅ Precision       | ~85%          |
| ✅ Recall          | ~89%          |
| ✅ mAP@0.5         | ~90%          |
| ⚡ Inference Speed | ~30 FPS (CPU) |

- *Precision:* The percentage of detected potholes that were actually potholes.  
- *Recall:* The percentage of real potholes that were successfully detected.  
- *mAP:* Mean Average Precision, a combined measure of model accuracy.  
- *Inference Speed:* Average speed of real-time detection on CPU.

These results make the model suitable for real-world applications such as smart city infrastructure monitoring, autonomous vehicles, and road maintenance systems.

---

## 🌟 Future Improvements

Here are some potential enhancements and next steps for this project:

- 🚀 *Cloud Deployment:* Host the application on platforms like AWS, Render, or Heroku for public access.  
- 📍 *GPS Integration:* Add location tracking to map potholes in real-time.  
- 📊 *Dashboard & Analytics:* Build a web dashboard to visualize detection data and trends.  
- 📱 *Mobile Application:* Develop a companion mobile app for field engineers and city inspectors.  
- 🧠 *Model Expansion:* Train on a larger, more diverse dataset to improve detection of different road conditions and pothole types.

---

## 👨‍💻 Author

*Moyinoluwa Idowu*  
📍 Computer Science Enthusiast | AI & Data Science | Smart Infrastructure Solutions  

📧 Email: Moyinoluwa.idowu24@gmail.com  
🔗 LinkedIn: [Moyinoluwa Idowu](https://www.linkedin.com/)  
🐙 GitHub: [Moyinoluwa Idowu](https://github.com/Emmanoel24)

💡 "Fixing roads is not just about asphalt — it's about saving lives. This project is a small step toward smarter cities and safer transportation."