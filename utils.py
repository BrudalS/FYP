import cv2
import numpy as np

def preprocess_image(image):
    """Preprocess image for emotion prediction."""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    resized_image = cv2.resize(gray, (48, 48))
    normalized_image = resized_image / 255.0
    return np.expand_dims(np.expand_dims(normalized_image, axis=-1), axis=0)

def predict_emotion(model, processed_image):
    """Predict the emotion using the pre-trained model."""
    prediction = model.predict(processed_image)
    emotion_index = np.argmax(prediction)
    return emotions[emotion_index]
