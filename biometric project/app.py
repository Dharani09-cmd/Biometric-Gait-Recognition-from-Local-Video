from flask import Flask, render_template, request
import cv2
import mediapipe as mp
import numpy as np
import os

app = Flask(__name__)
UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/upload', methods=['POST'])
def upload_video():
    if 'video' not in request.files:
        return render_template("index.html", result="No file selected")

    file = request.files['video']
    if file.filename == '':
        return render_template("index.html", result="No file selected")

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose()
    cap = cv2.VideoCapture(filepath)

    step_count = 0
    prev_y = None

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        results = pose.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        if results.pose_landmarks:
            y = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ANKLE].y
            if prev_y and abs(y - prev_y) > 0.05:
                step_count += 1
            prev_y = y

    cap.release()
    pose.close()

    result_text = f"Detected approximately {step_count//2} steps in the video."
    return render_template("index.html", result=result_text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
