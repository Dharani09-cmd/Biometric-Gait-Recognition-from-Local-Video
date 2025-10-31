from flask import Flask, jsonify, request
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.misc import imresize, imread
from human_pose_nn import HumanPoseIRNetwork
import os

mpl.use('Agg')
app = Flask(__name__)

# Load model once
net_pose = HumanPoseIRNetwork()
net_pose.restore('models/MPII+LSP.ckpt')

@app.route('/')
def home():
    return "✅ Biometric Gait Recognition API is running!"

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    image_file = request.files['image']
    image_path = os.path.join('images', image_file.filename)
    image_file.save(image_path)

    # Process image
    img = imread(image_path)
    img = imresize(img, [299, 299])
    img_batch = np.expand_dims(img, 0)

    y, x, a = net_pose.estimate_joints(img_batch)
    y, x, a = np.squeeze(y), np.squeeze(x), np.squeeze(a)

    joint_names = [
        'right ankle', 'right knee', 'right hip', 'left hip', 'left knee',
        'left ankle', 'pelvis', 'thorax', 'upper neck', 'head top',
        'right wrist', 'right elbow', 'right shoulder',
        'left shoulder', 'left elbow', 'left wrist'
    ]

    # Return results as JSON
    results = {joint_names[i]: float(a[i]) for i in range(len(joint_names))}
    return jsonify(results)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
