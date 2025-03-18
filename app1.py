import streamlit as st
import cv2
import numpy as np
import sqlite3
import pandas as pd
import os
import re
import base64
from ultralytics import YOLO
from paddleocr import PaddleOCR

# Function to Convert Image to Base64 (For Background)
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Function to Set Streamlit Background Image
def set_background(image_path):
    if os.path.exists(image_path):
        base64_img = get_base64_image(image_path)
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url("data:image/png;base64,{base64_img}");
                background-size: cover;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
set_background("bg.avif")  # Replace with correct file path

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

# Load the stolen vehicle dataset
stolen_vehicles_df = pd.read_csv("stolen_vehicles_large.csv")

# Load YOLOv11 Model
model = YOLO("best_69.pt")

# Initialize PaddleOCR for License Plate Recognition
ocr = PaddleOCR(use_angle_cls=True, use_gpu=False)

# Setup SQLite Database for storing detected plates
def setup_database():
    conn = sqlite3.connect("licensePlatesDatabase.db")
    cursor = conn.cursor()
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS LicensePlates(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            license_plate TEXT UNIQUE,
            confidence REAL,
            status TEXT
        )
        '''
    )
    conn.commit()
    conn.close()

setup_database()

# Function to check if a vehicle is stolen
def is_vehicle_stolen(plate_number):
    return plate_number in stolen_vehicles_df["License Plate"].values

# Function to perform OCR on a detected license plate
def paddle_ocr(frame, x1, y1, x2, y2):
    plate_img = frame[y1:y2, x1:x2]  # Crop the license plate area
    plate_img = cv2.resize(plate_img, (300, 100))  # Resize for better OCR
    result = ocr.ocr(plate_img, det=False, rec=True, cls=False)

    text, confidence = "", 0
    for r in result:
        if isinstance(r, list) and len(r) > 0:
            detected_text, conf_score = r[0]
            confidence = 0 if np.isnan(conf_score) else round(conf_score * 100, 2)
            if confidence > 60:  # Consider only high-confidence results
                text = detected_text

    # Clean up detected text
    pattern = re.compile('[\W]')
    text = pattern.sub('', text).replace("???", "").replace("O", "0").replace("粤", "")
    return text.upper(), confidence

# Function to save detected plates to the database
def save_to_database(plate, conf):
    conn = sqlite3.connect("licensePlatesDatabase.db")
    cursor = conn.cursor()
    status = "Stolen" if is_vehicle_stolen(plate) else "Not Stolen"
    cursor.execute(
        '''INSERT OR REPLACE INTO LicensePlates(license_plate, confidence, status) VALUES (?, ?, ?)''',
        (plate, conf, status)
    )
    conn.commit()
    conn.close()

# Function to draw bounding boxes (without text overlay)
def draw_boxes(image, results):
    detected_plates = []
    
    for result in results:
        if hasattr(result, "boxes"):
            for box in result.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                plate_number, ocr_conf = paddle_ocr(image, x1, y1, x2, y2)

                if plate_number and ocr_conf > 60:
                    # Draw bounding box only (no text overlay)
                    cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 3)
                    detected_plates.append((plate_number, ocr_conf))

    return image, detected_plates

# Streamlit UI Setup
st.title("License Plate Recognition & Stolen Vehicle Detection")

# File Upload (Image or Video)
uploaded_file = st.file_uploader("Upload Image or Video", type=["jpg", "jpeg", "png", "mp4"])

if uploaded_file:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)

    # Processing Image Upload
    if uploaded_file.type in ["image/jpeg", "image/png"]:
        image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
        results = model(image, conf=0.3)  # Lower confidence threshold for better detection
        processed_image, detected_plates = draw_boxes(image, results)  # Draw bounding boxes

        # Show detected plates separately
        st.subheader("📌 Detected License Plates:")
        for plate, conf in detected_plates:
            status = "Stolen" if is_vehicle_stolen(plate) else "Not Stolen"
            st.write(f"**Plate:** `{plate}` - **Confidence:** {conf}% - **Status:** `{status}`")
            save_to_database(plate, conf)  # Save to database

        st.image(processed_image, caption="Processed Image with License Plate", use_column_width=True)

    # Processing Video Upload
    elif uploaded_file.type == "video/mp4":
        st.video(uploaded_file)
        temp_video_path = "temp_video.mp4"
        with open(temp_video_path, "wb") as f:
            f.write(uploaded_file.getvalue())

        cap = cv2.VideoCapture(temp_video_path)
        frame_count = 0
        detected_plates_set = set()  # To avoid duplicate entries in the same video

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            frame_count += 1

            if frame_count % 5 == 0:  # Process every 5th frame for efficiency
                results = model(frame, conf=0.3)  # Run YOLO detection
                _, detected_plates = draw_boxes(frame, results)  # Get detected plates
                
                for plate, conf in detected_plates:
                    if plate not in detected_plates_set:  # Avoid duplicate storage
                        detected_plates_set.add(plate)  
                        status = "Stolen" if is_vehicle_stolen(plate) else "Not Stolen"
                        save_to_database(plate, conf)  # Store in database
                        st.write(f"**Detected:** `{plate}` - **Confidence:** {conf}% - **Status:** `{status}`")

        cap.release()
        os.remove(temp_video_path)  # Remove temp video after processing

        st.write("✅ Video Processing Completed. All detected plates stored in the database.")

# Sidebar: Show Database Records
st.sidebar.header("📜 Database Records")
if st.sidebar.button("🔍 Show Stored Plates"):
    conn = sqlite3.connect("licensePlatesDatabase.db")
    df = pd.read_sql("SELECT * FROM LicensePlates", conn)
    st.sidebar.dataframe(df)