import requests
import cv2
import io

def send_image_to_server(image):
    """Send image to the server to detect emotion."""
    url = 'http://<your-server-ip>:5000/detect_emotion'
    
    # Convert image to byte array
    _, img_encoded = cv2.imencode('.jpg', image)
    img_bytes = img_encoded.tobytes()
    
    files = {'image': io.BytesIO(img_bytes)}
    response = requests.post(url, files=files)
    
    if response.status_code == 200:
        emotion = response.json().get('emotion')
        print(f"Detected Emotion: {emotion}")
        return emotion
    else:
        print("Error in detecting emotion.")
        return None
