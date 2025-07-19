Hand Gesture Recognition & Volume Control
Overview
This project demonstrates real-time hand gesture recognition and gesture-based system volume control using OpenCV and MediaPipe. It allows recognition of basic gestures (like open palm, fist, thumbs up/down) and lets users adjust their computer’s audio volume with simple hand movements—all using a standard webcam.

Features
Gesture Recognition: Detects common hand gestures—open palm, fist, thumbs up, thumbs down—using webcam video and the MediaPipe Hands library.

Gesture-Based Volume Control: Adjusts system audio volume up or down based on the distance between thumb and index finger, leveraging pyautogui for keyboard interaction.

Real-Time Feedback: Displays detected gestures and actions live on the video feed with clear on-screen annotations.

Easy to Use: Works with any standard laptop/PC webcam.

Technologies Used
Python 3.x

OpenCV (cv2) — for video capture and image processing

MediaPipe — for accurate hand landmark detection

pyautogui — for automating system volume control (only in volume control script)

How It Works
1. Gesture Recognition (hand.py)
Captures webcam feed.

Detects hand landmarks with MediaPipe.

Classifies gestures:

Open Palm: All fingers extended.

Fist: All fingers curled.

Thumbs Up/Down: Only thumb extended upwards or downwards, respectively.

Displays recognized gesture on the video screen in real time.

2. Volume Control (hand_volume.py)
Captures the position of the index finger tip and thumb tip.

Calculates their distance:

If the distance is large, increases volume.

If the distance is small, decreases volume.

Draws circles at keypoints and a line connecting thumb and index finger.

Uses the pyautogui library to simulate "volume up" and "volume down" keypresses.

Usage
Install dependencies:

bash
pip install opencv-python mediapipe pyautogui
Run Gesture Recognition:

bash
python hand.py
Press q to exit.

Run Hand Volume Control:

bash
python hand_volume.py
Press Esc to exit.

Ensure your webcam is connected and accessible.

Sample Gestures
Show an open palm: Should display "Open Palm".

Make a fist: Should display "Fist".

Thumbs up/down: Should display the corresponding gesture.

Move thumb and index finger apart (in hand_volume.py): Volume goes up.

Bring thumb and index finger closer (in hand_volume.py): Volume goes down.

Applications
Touchless control for accessibility and intuitive user interfaces.

Assistive technology for users with limited mobility.

Interactive systems in gaming, media, and smart home control.

Credits
Built by Jatin Bagga
Leveraging OpenCV, MediaPipe, and Python for interactive computer vision applications.
