from datetime import datetime
from time import sleep

from bson import ObjectId
from pymongo import MongoClient
import cv2
import numpy as np
from deepface import DeepFace
from os import getcwd, path, remove
import pandas as pd
import pytz

client = MongoClient("mongodb+srv://jakulerogod69:jakulerogods@jaja.uvxgo.mongodb.net/?retryWrites=true&w=majority&appName=jaja")
db = client["Attendance"]

attendance = db["Attendance"]
student = db["Student"]


# Get the absolute path of the current working directory
base_path = path.abspath(getcwd())
print(f"Base Path: {base_path}")

# Initialize webcam feed (0 is the default webcam, change if necessary)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not access the webcam.")
    exit()

sleep(1)

while True:
    # Capture frame-by-frame from the webcam
    ret, frame = cap.read()

    if not ret:
        print("Failed to grab frame")
        break

    # Convert the captured frame to RGB (DeepFace expects RGB input)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Save the frame temporarily to use in DeepFace.find()
    temp_frame_path = path.join(base_path, "temp_frame.jpg")
    cv2.imwrite(temp_frame_path, frame)  # Save the frame as a temporary image

    # Perform facial recognition with DeepFace
    try:
        # Find matches in the "selections" folder with enforce_detection=False
        match = DeepFace.find(
            temp_frame_path,  # Use the temporary frame as input
            path.join(base_path, "selections"),  # Folder to search for matches
            enforce_detection=False,  # Disable face detection
            model_name="VGG-Face"
        )
        # VGG-Face, Facenet, Facenet512, OpenFace, DeepFace, DeepID, Dlib, ArcFace, SFace and GhostFaceNet

        # Check if matches are found and display the results
        if match:
            # The result will contain a 'identity' key with the matched image paths
            matched_images = [m['identity'][0] for m in match]
            print(f"Matched images: {matched_images}")
            id = path.basename(matched_images[0]).split(".")[0]
            inserted = attendance.insert_one({"student_id": ObjectId(id), "time": datetime.now(tz=pytz.timezone("Asia/Manila"))})
            print(inserted)
            # look for student record

            # You can display the name of the matched image on the frame
            for matched_image in matched_images:
                cv2.putText(frame, f"Match: {path.basename(matched_image)}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            break

    except Exception as e:
        print(f"Error during DeepFace processing: {e}")

    # Show the frame with the matched results
    cv2.imshow('Webcam Feed', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close OpenCV windows
cap.release()
cv2.destroyAllWindows()


if path.exists(temp_frame_path):
    remove(temp_frame_path)


# Fast API
# HTMX