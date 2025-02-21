from flask import Flask, request, jsonify

app = Flask(__name__)

# Store detected emotions
emotion_log = []

@app.route('/')
def index():
    return "Emotion Detection Server is Running!"

# Store emotion from local processing
@app.route('/store_emotion', methods=['POST'])
def store_emotion():
    data = request.get_json()
    if not data or 'emotion' not in data:
        return jsonify({'error': 'No emotion data provided!'}), 400
    
    emotion = data['emotion']
    emotion_log.append(emotion)
    return jsonify({"status": "success", "message": f"Emotion '{emotion}' stored successfully!"})

# Retrieve stored emotions
@app.route('/get_emotions', methods=['GET'])
def get_emotions():
    return jsonify({"emotions": emotion_log})

# Switch to manual mode
@app.route('/switch_to_manual', methods=['POST'])
def switch_to_manual():
    return jsonify({"status": "manual_mode", "message": "Manual Mode activated!"})

# Switch to intelligent mode
@app.route('/switch_to_intelligent', methods=['POST'])
def switch_to_intelligent():
    return jsonify({"status": "intelligent_mode", "message": "Intelligent Mode activated!"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
