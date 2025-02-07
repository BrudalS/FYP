from flask import Flask, request, jsonify
import tensorflow as tf
import cv2
import numpy as np
from utils import preprocess_image, predict_emotion
from keras.models import load_model

app = Flask(__name__)

# Load pre-trained emotion detection model
model = load_model('model/emotion_model.h5')

# Emotion labels
emotions = ["Happy", "Sad", "Surprise", "Anger", "Fear"]

@app.route('/')
def index():
    return "Emotion Detection Server is Running!"

# Emotion detection route
@app.route('/detect_emotion', methods=['POST'])
def detect_emotion():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file found!'}), 400
    
    image_file = request.files['image']
    img = np.asarray(bytearray(image_file.read()))
    img = cv2.imdecode(img, cv2.IMREAD_COLOR)

    # Preprocess image and predict emotion
    processed_image = preprocess_image(img)
    emotion = predict_emotion(model, processed_image)

    # Return predicted emotion
    return jsonify({"emotion": emotion})

# Switch to manual mode
@app.route('/switch_to_manual', methods=['POST'])
def switch_to_manual():
    # Add logic for manual mode here
    return jsonify({"status": "manual_mode", "message": "Manual Mode activated!"})

# Switch to intelligent mode
@app.route('/switch_to_intelligent', methods=['POST'])
def switch_to_intelligent():
    # Add logic for intelligent mode here
    return jsonify({"status": "intelligent_mode", "message": "Intelligent Mode activated!"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
