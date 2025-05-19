from flask import Flask, render_template, request, jsonify
import cv2
import numpy as np
import base64
import time
import face_recognition
import music_player

app = Flask(__name__)

last_detected_time = 0  # Prevents too fast detections

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/detect_emotion", methods=["POST"])
def detect_emotion():
    global last_detected_time
    current_time = time.time()

    # Prevents rapid multiple detections within 2 seconds
    if current_time - last_detected_time < 2:
        return jsonify({"emotion": "Wait before detecting again"})

    data = request.json
    image_data = base64.b64decode(data["image"].split(",")[1])
    np_arr = np.frombuffer(image_data, np.uint8)
    frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    emotion = face_recognition.detect_emotion(frame)

    if emotion == "No Face Detected":
        return jsonify({"emotion": "No Face Detected. Try Again!"})

    music_player.play_music(emotion)
    last_detected_time = current_time  # Update last detected time

    return jsonify({"emotion": emotion})

if __name__ == "__main__":
    app.run(debug=True)
