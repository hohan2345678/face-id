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

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to the actual frontend origin for security (e.g., ["http://localhost:3000"])
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

# MongoDB Connection
client = MongoClient("mongodb+srv://jakulerogod69:jakulerogods@jaja.uvxgo.mongodb.net/?retryWrites=true&w=majority&appName=jaja")
db = client["Attendance"]
attendance = db["Attendance"]

# Base directory
base_path = path.abspath(getcwd())

@app.get("/detect-face/")
async def detect_face():
    """Opens the webcam, captures an image, and performs face recognition."""
    try:
        cap = cv2.VideoCapture(0)  # Open webcam

        if not cap.isOpened():
            return {"status": "error", "message": "Could not access the webcam"}

        ret, frame = cap.read()
        cap.release()  # Release the webcam after capturing

        if not ret:
            return {"status": "error", "message": "Failed to capture image from webcam"}

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

