# 🔍 License Plate Recognition for Detecting Stolen Vehicles

A real-time, intelligent system that detects license plates from vehicle images/videos and cross-verifies them against a stolen vehicles database. Built using YOLOv8, PaddleOCR, and Streamlit, this project aims to enhance security and surveillance applications through automated number plate recognition (ANPR).

---

## 📑 Table of Contents

- [🔧 Features](#-features)
- [🧠 Tech Stack](#-tech-stack)
- [🚀 How It Works](#-how-it-works)
- [⚙️ Installation](#️-installation)
- [🌐 Running the App](#-running-the-app)
- [🧪 Example Results](#-example-results)
- [📦 Datasets & Models](#-datasets--models)
- [📌 Future Enhancements](#-future-enhancements)
- [🤝 Contributors](#-contributors)
- [📄 License](#-license)

---

## 🔧 Features

- 🚘 Upload images or videos to detect vehicle license plates
- 🧠 License plate detection using **YOLOv8**
- 🔤 Text extraction using **PaddleOCR**
- 📋 Match against a **stolen vehicles database**
- 📸 Real-time frame-by-frame video analysis
- 📊 Stores all detections in a SQLite database
- 🌈 Clean, user-friendly **Streamlit UI**
- 🎨 Custom background support (base64-encoded)

---

## 🧠 Tech Stack

| Layer         | Technology                              |
|---------------|------------------------------------------|
| Frontend      | Streamlit, HTML/CSS                      |
| Backend       | Python                                   |
| CV Models     | YOLOv11 (Ultralytics), PaddleOCR          |
| Database      | SQLite (for detections), CSV (stolen data)|
| Other Tools   | OpenCV, NumPy, Pandas, PIL               |

---

## 🚀 How It Works

1. **Upload** an image or video.
2. **Detect** license plates using a YOLOv8 custom model.
3. **Extract text** from plates using PaddleOCR.
4. **Check** if the plate exists in the `stolen_vehicles.csv`.
5. **Store results** in SQLite for record keeping.
6. **Display** results with visual bounding boxes and status messages.

---

## ⚙️ Installation

```bash
# 1. Clone the repository
git clone https://github.com/GudiseMeghana/LICENSE-PLATE-RECOGNITION-FOR-DETECTING-STOLEN-VEHICLES.git
cd LICENSE-PLATE-RECOGNITION-FOR-DETECTING-STOLEN-VEHICLES

# 2. Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# 3. Install dependencies
pip install -r requirements.txt
