# 🔍 License Plate Recognition for Detecting Stolen Vehicles

![License](https://img.shields.io/github/license/GudiseMeghana/LICENSE-PLATE-RECOGNITION-FOR-DETECTING-STOLEN-VEHICLES)
![Stars](https://img.shields.io/github/stars/GudiseMeghana/LICENSE-PLATE-RECOGNITION-FOR-DETECTING-STOLEN-VEHICLES)
![Issues](https://img.shields.io/github/issues/GudiseMeghana/LICENSE-PLATE-RECOGNITION-FOR-DETECTING-STOLEN-VEHICLES)

## 🚗 Overview

A real-time, intelligent system to detect vehicle license plates from images or videos and cross-check against a database of stolen vehicles. Built with **YOLOv11**, **PaddleOCR**, and **Streamlit** for modern, robust performance.

---

## 📑 Table of Contents

- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Quick Start](#-quick-start)
- [Installation](#-installation)
- [How It Works](#-how-it-works)
- [Example Results](#-example-results)
- [Configuration](#-configuration)
- [Datasets & Models](#-datasets--models)
- [Troubleshooting](#-troubleshooting)
- [Future Enhancements](#-future-enhancements)
- [Contributors](#-contributors)
- [License](#-license)

---

## 🔧 Features

- Upload images or videos to detect vehicle license plates
- License plate detection using **YOLOv11**
- Text extraction with **PaddleOCR**
- Match against a **stolen vehicles database**
- Live, frame-by-frame video analysis
- Stores all detections in a SQLite database
- Clean, user-friendly **Streamlit UI**
- Custom background support (base64-encoded)

---

## 🧠 Tech Stack

| Layer         | Technology                          |
|---------------|-------------------------------------|
| Frontend      | Streamlit, HTML/CSS                 |
| Backend       | Python                              |
| CV Models     | YOLOv11 (Ultralytics), PaddleOCR    |
| Database      | SQLite, CSV (stolen data)           |
| Other Tools   | OpenCV, NumPy, Pandas, PIL          |

---

## ⚡ Quick Start

```bash
git clone https://github.com/GudiseMeghana/LICENSE-PLATE-RECOGNITION-FOR-DETECTING-STOLEN-VEHICLES.git
cd LICENSE-PLATE-RECOGNITION-FOR-DETECTING-STOLEN-VEHICLES
pip install -r requirements.txt
streamlit run app1.py
```

---

## ⚙️ Installation

1. **Clone the repository**
2. **Create a virtual environment (recommended)**
3. **Install the dependencies**

Detailed steps:
```bash
git clone https://github.com/GudiseMeghana/LICENSE-PLATE-RECOGNITION-FOR-DETECTING-STOLEN-VEHICLES.git
cd LICENSE-PLATE-RECOGNITION-FOR-DETECTING-STOLEN-VEHICLES
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
pip install -r requirements.txt
```

---

## 🚀 How It Works

1. **Upload** an image or video.
2. **Detect** license plates via YOLOv11.
3. **Extract** plate text using PaddleOCR.
4. **Check** against the `stolen_vehicles.csv` database.
5. **Store** results in SQLite for records.
6. **Display** bounding boxes and status on results.

---

## 🧪 Example Results

![Example Result 1](https://github.com/user-attachments/assets/5d998730-23e4-4595-b80b-86ab5203cc0d)
![Example Result 2](https://github.com/user-attachments/assets/c1bececd-ddbe-4ecb-a6ae-698af0c9d3ff)

---

## ⚙️ Configuration

- **stolen_vehicles_large.csv:** Place your CSV with stolen vehicles in the root directory.
- **Database:** Detected plates are stored in `licensePlatesDatabase.db`
- **Model Files:** Ensure `best_69.pt` and `yolo11n.pt` are present.

---

## 📦 Datasets & Models

- **YOLOv11 Model:** Trained on a custom dataset of license plates.
- **PaddleOCR:** Pre-trained English model.
- **Stolen Vehicles Dataset:** `stolen_vehicles_large.csv` with known stolen plates.

---

## 🛠️ Troubleshooting

- *Streamlit not found?* Run `pip install streamlit`
- *Model loading errors?* Ensure model weights are in the project root.
- *OCR issues?* Check PaddleOCR installation and language pack.

---

## 📌 Future Enhancements

- Real-time live camera support
- API endpoints (FastAPI)
- Dashboard authentication
- Mobile version (PWA)
- Export logs to Excel/PDF
- MQTT/WebSocket for IoT integration

---

## 🤝 Contributors

We welcome contributions! Please read our [contributing guidelines](CONTRIBUTING.md) and open a pull request.

---

## 📫 Contact & Support

For issues, please [open a GitHub issue](https://github.com/GudiseMeghana/LICENSE-PLATE-RECOGNITION-FOR-DETECTING-STOLEN-VEHICLES/issues).

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

