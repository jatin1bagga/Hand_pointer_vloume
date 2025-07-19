import cv2
import mediapipe as mp

# Initialize Mediapipe Hand module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)
mp_draw = mp.solutions.drawing_utils

# Open webcam
cap = cv2.VideoCapture(0)

def detect_gesture(landmarks, frame):
    h, w, _ = frame.shape
    # Get landmark positions in pixels
    lm = [(int(l.x * w), int(l.y * h)) for l in landmarks.landmark]

    # Open Palm: All fingertips above their respective lower joints
    if lm[8][1] < lm[6][1] and lm[12][1] < lm[10][1] and lm[16][1] < lm[14][1] and lm[20][1] < lm[18][1]:
        return "Open Palm"

    # Fist: All fingertips below their respective lower joints
    elif lm[8][1] > lm[6][1] and lm[12][1] > lm[10][1] and lm[16][1] > lm[14][1] and lm[20][1] > lm[18][1]:
        return "Fist"

    # Thumbs Up: Thumb extended up, other fingers curled
    elif lm[4][1] < lm[3][1] and lm[8][1] > lm[6][1] and lm[12][1] > lm[10][1] and lm[16][1] > lm[14][1] and lm[20][1] > lm[18][1]:
        return "Thumbs Up"

    # Thumbs Down: Thumb extended down, other fingers curled
    elif lm[4][1] > lm[3][1] and lm[8][1] > lm[6][1] and lm[12][1] > lm[10][1] and lm[16][1] > lm[14][1] and lm[20][1] > lm[18][1]:
        return "Thumbs Down"

    return "Unknown"

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert frame to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Detect gesture and display it
            gesture = detect_gesture(hand_landmarks, frame)
            cv2.putText(frame, gesture, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    # Show output
    cv2.imshow("Hand Gesture Recognition", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
