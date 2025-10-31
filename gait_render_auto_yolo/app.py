
from flask import Flask, request, render_template, jsonify, send_from_directory
import os
from PIL import Image
import io
import base64

app = Flask(__name__, static_folder='static', template_folder='templates')

MODEL = None
USE_ULTRALYTICS = False

try:
    from ultralytics import YOLO
    import torch

    model_path = os.path.join('models', 'yolov8n.pt')
    os.makedirs('models', exist_ok=True)
    if not os.path.exists(model_path):
        print("Downloading YOLOv8n model...")
        YOLO('yolov8n.pt')  # triggers auto-download into cache
        import shutil
        cached = os.path.expanduser('~/.cache/torch/hub/ultralytics_yolov5_master/yolov8n.pt')
        if os.path.exists(cached):
            shutil.copy(cached, model_path)
    MODEL = YOLO(model_path)
    USE_ULTRALYTICS = True
    print("YOLOv8 model loaded successfully.")
except Exception as e:
    print("Could not load YOLOv8 model:", e)
    USE_ULTRALYTICS = False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'no image uploaded'}), 400
    file = request.files['image']
    img_bytes = file.read()
    try:
        img = Image.open(io.BytesIO(img_bytes)).convert('RGB')
    except Exception as e:
        return jsonify({'error': 'invalid image', 'detail': str(e)}), 400

    if USE_ULTRALYTICS and MODEL is not None:
        try:
            results = MODEL.predict(source=img, imgsz=640, device='cpu')
            detections = []
            for r in results:
                for b in r.boxes:
                    xyxy = b.xyxy.tolist()[0]
                    conf = float(b.conf.tolist()[0])
                    cls = int(b.cls.tolist()[0])
                    detections.append({'xyxy': xyxy, 'conf': conf, 'class': cls})
            return jsonify({'mock': False, 'detections': detections})
        except Exception as e:
            return jsonify({'error': 'model inference failed', 'detail': str(e)}), 500

    # Fallback mock
    width, height = img.size
    detections = [
        {'xyxy': [width*0.1, height*0.2, width*0.3, height*0.7], 'conf': 0.85, 'class': 0},
        {'xyxy': [width*0.5, height*0.15, width*0.75, height*0.8], 'conf': 0.78, 'class': 0}
    ]
    return jsonify({'mock': True, 'detections': detections})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
