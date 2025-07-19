# ✋ Hand Gesture Recognition & Volume Control 🎚️

This project uses **OpenCV**, **MediaPipe**, and **Python** to recognize hand gestures in real-time using a webcam and allows you to **control system volume** by measuring the distance between your thumb and index finger.

---

## 📌 Features

- ✋ **Gesture Recognition**: Detects common hand gestures like:
  - Open Palm 🖐️
  - Fist ✊
  - Thumbs Up 👍
  - Thumbs Down 👎

- 🔊 **Gesture-Based Volume Control**:
  - Moves your thumb and index finger apart → Volume Up
  - Brings thumb and index finger closer → Volume Down

- 🖥️ **Real-Time Feedback**: All recognized gestures and actions are shown live on-screen.

- 🎥 **Webcam Friendly**: Works with any laptop/desktop webcam.

---

## 🧰 Technologies Used

- **Python 3.x**
- `OpenCV` — for video capture and image processing
- `MediaPipe` — for hand tracking and landmark detection
- `pyautogui` — for simulating volume key presses *(volume control only)*

---

## ⚙️ How It Works

### 1. `hand.py` - Gesture Recognition

- Captures video feed using webcam
- Detects hand landmarks with MediaPipe
- Classifies hand pose based on finger positions:
  - All fingers up → **Open Palm**
  - All fingers down → **Fist**
  - Only thumb up/down → **Thumbs Up / Down**
- Displays gesture name on-screen

---

### 2. `hand_volume.py` - Volume Control

- Detects thumb and index finger tip
- Calculates Euclidean distance between them
- Interprets the distance as volume control:
  - Large distance = 🔊 Volume Up
  - Small distance = 🔉 Volume Down
- Simulates volume key presses using `pyautogui`

---

## 💻 Installation & Usage

### 1. Install Dependencies

```bash
pip install opencv-python mediapipe pyautogui
