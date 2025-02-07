function switchMode(mode) {
    fetch(`http://<your-server-ip>:5000/switch_to_${mode}`, {
        method: 'POST'
    }).then(response => response.json())
      .then(data => {
          alert(data.message);
      });
}

function detectEmotion() {
    fetch('http://<your-server-ip>:5000/detect_emotion', {
        method: 'POST',
        body: JSON.stringify({ /* Camera Image Data */ })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('emotionResult').innerText = `Detected Emotion: ${data.emotion}`;
    });
}
