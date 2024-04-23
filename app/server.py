# app/server.py

from flask import Flask, request, jsonify
from app.emotion import emotion_predictor

app = Flask(__name__)

@app.route('/detect-emotion', methods=['POST'])
def detect_emotion():
    text = request.json.get('text')
    if not text:
        return jsonify({"error": "No text provided"}), 400
    emotions = emotion_predictor(text)
    return jsonify(emotions)

if __name__ == "__main__":
    app.run(debug=True)
