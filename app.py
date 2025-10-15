from flask import Flask, render_template, request
import os
import cv2
import numpy as np
import mediapipe as mp

app = Flask(__name__)
UPLOAD_FOLDER = 'videos'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

mp_pose = mp.solutions.pose

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_video():
    if 'video' not in request.files:
        return "No video uploaded", 400
    
    video = request.files['video']
    video_path = os.path.join(UPLOAD_FOLDER, video.filename)
    video.save(video_path)

    result = process_video(video_path)
    return render_template('index.html', result=result)

def process_video(video_path):
    cap = cv2.VideoCapture(video_path)
    joint_data = []
    with mp_pose.Pose(static_image_mode=False) as pose:
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = pose.process(frame_rgb)
            if results.pose_landmarks:
                joints = [(lm.x, lm.y) for lm in results.pose_landmarks.landmark]
                joint_data.append(joints)
    cap.release()

    if not joint_data:
        return "No person detected in video."

    joint_array = np.array(joint_data).reshape(len(joint_data), -1)
    fft_features = np.fft.fft(joint_array, axis=0)
    fft_magnitude = np.abs(fft_features)
    result = f"Video processed successfully! Frames: {joint_array.shape[0]}, FFT Mean: {fft_magnitude.mean():.2f}"
    return result

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
