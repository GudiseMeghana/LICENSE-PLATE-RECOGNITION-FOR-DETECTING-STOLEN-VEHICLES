# 🔍 License Plate Recognition for Detecting Stolen Vehicles

A real-time, intelligent system that detects license plates from vehicle images/videos and cross-verifies them against a stolen vehicles database. Built using YOLOv11, PaddleOCR, and Streamlit, this project provides a user-friendly interface for efficient license plate recognition and validation.

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
- 🧠 License plate detection using **YOLOv11**
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
| Frontend      | Streamlit, HTML/CSS                     |
| Backend       | Python                                  |
| CV Models     | YOLOv11 (Ultralytics), PaddleOCR         |
| Database      | SQLite (for detections), CSV (stolen data) |
| Other Tools   | OpenCV, NumPy, Pandas, PIL              |

---

## 🚀 How It Works

1. **Upload** an image or video.
2. **Detect** license plates using a YOLOv11 custom model.
3. **Extract text** from plates using PaddleOCR.
4. **Check** if the plate exists in the `stolen_vehicles.csv`.
5. **Store results** in SQLite for record keeping.
6. **Display** results with visual bounding boxes and status messages.

---

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/GudiseMeghana/LICENSE-PLATE-RECOGNITION-FOR-DETECTING-STOLEN-VEHICLES.git
   cd LICENSE-PLATE-RECOGNITION-FOR-DETECTING-STOLEN-VEHICLES
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🌐 Running the App

Run the application using Streamlit:

```bash
streamlit run app1.py
```


---

## 🧪 Example Results

Below are sample outputs from the system:

![Example Result 1](https://github.com/user-attachments/assets/5d998730-23e4-4595-b80b-86ab5203cc0d)
![Example Result 2](https://github.com/user-attachments/assets/c1bececd-ddbe-4ecb-a6ae-698af0c9d3ff)

---

## 📦 Datasets & Models

- **YOLOv11 Model**: Trained on a custom dataset of license plates.
- **PaddleOCR**: Pre-trained English model with angle classification.
- **Stolen Vehicles Dataset**: `stolen_vehicles.csv` containing known stolen plates.

---

## 📌 Future Enhancements

- 🔁 Real-time live camera support
- 🌐 API endpoints using FastAPI
- 🔒 Authentication for dashboard access
- 📲 Mobile version (PWA)
- 📤 Export logs to Excel or PDF
- 📡 MQTT or WebSocket for smart surveillance use cases

---

## 🤝 Contributors

We welcome contributions! Feel free to fork the repository and submit a pull request.

---

## 📄 License

This project is licensed under the MIT License. See the LICENSE file for details.
