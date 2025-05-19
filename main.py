import cv2
import face_recognition
import music_player

# Start video capture
cap = cv2.VideoCapture(0)

last_emotion = None  # Track the last detected emotion

while True:
    ret, frame = cap.read()
    if not ret:
        break

    emotion = face_recognition.detect_emotion(frame)
    print(f"Detected Emotion: {emotion}")

    # Play music only if the emotion has changed
    if emotion != last_emotion:
        music_player.play_music(emotion)
        last_emotion = emotion  # Update last detected emotion

    cv2.imshow("Emotion Detector", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):  # Press 'q' to quit
        break

cap.release()
cv2.destroyAllWindows()
