import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Load pre-trained emotion detection model
try:
    model = load_model("emotion_model.h5", compile=False)
except Exception as e:
    print(f"Error: Could not load emotion model! {e}")
    exit()

# Load Haarcascade face detector
cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(cascade_path)

if face_cascade.empty():
    print("Error: Haarcascade file not found! Check the path.")
    exit()

# Define emotion labels
EMOTIONS = ["Angry", "Disgust", "Fear", "Happy", "Neutral", "Sad", "Surprise"]

def detect_emotion(frame):
    """Detects facial expression and returns the emotion label."""
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=6, minSize=(50, 50))

    if len(faces) == 0:
        return "No Face Detected"

    for (x, y, w, h) in faces:
        face = gray[y:y+h, x:x+w]
        face = cv2.resize(face, (48, 48))  # Resize for the model
        face = face / 255.0  # Normalize pixel values
        face = np.expand_dims(face, axis=-1)  # Add depth dimension
        face = np.expand_dims(face, axis=0)   # Add batch dimension

        prediction = model.predict(face)
        emotion_index = np.argmax(prediction)

        # Set confidence threshold to avoid incorrect predictions
        confidence = np.max(prediction)
        if confidence < 0.5:  
            return "Neutral"

        return EMOTIONS[emotion_index]

    return "Neutral"
