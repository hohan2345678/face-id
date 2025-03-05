from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime
from os import path, getcwd, remove
import pytz
import cv2
import numpy as np
from deepface import DeepFace
from pyzbar.pyzbar import decode 

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"], 
)

# MongoDB Connection
client = MongoClient("mongodb+srv://jakulerogod69:jakulerogods@jaja.uvxgo.mongodb.net/?retryWrites=true&w=majority&appName=jaja")
db = client["Attendance"]
attendance = db["Attendance"]

# Base directory
base_path = path.abspath(getcwd())

@app.get("/detect-face")
async def detect_face():
    """Opens the webcam, displays a window, captures an image, and performs face recognition."""
    try:
        cap = cv2.VideoCapture(0)  # Open webcam

        if not cap.isOpened():
            return {"status": "error", "message": "Could not access the webcam"}

        while True:
            ret, frame = cap.read()
            if not ret:
                cap.release()
                return {"status": "error", "message": "Failed to capture image from webcam"}
            
            cv2.imshow("Face Detection - Press 's' to capture", frame)
            key = cv2.waitKey(1) & 0xFF
            if key == ord('s'):
                break
        
        cap.release()
        cv2.destroyAllWindows()

        # Save the captured frame temporarily
        temp_frame_path = path.join(base_path, "temp_frame.jpg")
        cv2.imwrite(temp_frame_path, frame)

        # Perform face recognition
        match = DeepFace.find(
            temp_frame_path,
            path.join(base_path, "selections"),
            enforce_detection=False,
            model_name="VGG-Face"
        )

        # Remove the temp image
        if path.exists(temp_frame_path):
            remove(temp_frame_path)

        if match and 'identity' in match[0] and len(match[0]['identity']) > 0:
            matched_image = match[0]['identity'][0]
            student_id = path.basename(matched_image).split(".")[0]

            # Save attendance record in MongoDB
            inserted = attendance.insert_one({
                "student_id": ObjectId(student_id),
                "time": datetime.now(tz=pytz.timezone("Asia/Manila"))
            })

            return {"status": "success", "student_id": student_id, "attendance_id": str(inserted.inserted_id)}
        else:
            return {"status": "failed", "message": "No match found"}

    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.get("/scan-qr")
async def scan_qr():
    """Opens the webcam, displays a window, scans for QR code, and records attendance."""
    try:
        cap = cv2.VideoCapture(0)  # Open webcam

        if not cap.isOpened():
            return {"status": "error", "message": "Could not access the webcam"}

        while True:
            ret, frame = cap.read()
            if not ret:
                cap.release()
                return {"status": "error", "message": "Failed to capture image from webcam"}
            
            cv2.imshow("QR Scanner - Press 's' to scan", frame)
            key = cv2.waitKey(1) & 0xFF
            if key == ord('s'):
                break
        
        cap.release()
        cv2.destroyAllWindows()

        # Decode QR code(s) in the captured frame
        decoded_objects = decode(frame)
        
        if not decoded_objects:
            return {"status": "failed", "message": "No QR code detected"}

        # Assuming that there is only one QR code, use the first decoded object
        qr_data = decoded_objects[0].data.decode("utf-8")

        # Save attendance record in MongoDB
        inserted = attendance.insert_one({
            "student_id": qr_data, 
            "time": datetime.now(tz=pytz.timezone("Asia/Manila"))
        })

        return {"status": "success", "student_id": qr_data, "attendance_id": str(inserted.inserted_id)}

    except Exception as e:
        return {"status": "error", "message": str(e)}