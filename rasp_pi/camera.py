import cv2

def capture_image():
    """Capture image from Raspberry Pi camera."""
    cap = cv2.VideoCapture(0)  # 0 for the default camera
    ret, frame = cap.read()
    cap.release()
    return frame
