# ✋ Hand Gesture Volume Control Using OpenCV + MediaPipe

A real-time hand-gesture-based system that controls your computer’s volume using just two fingers — powered by **OpenCV**, **MediaPipe**, and **PyAutoGUI**.

---

### 🎬 Project Demo
(https://github.com/Ayancoder1/Hand_Gesture_Volume_Control/blob/main/HandgestureVolumeControlVideo.mp4)
---
## What Is This Project?

This is a **gesture-controlled volume system** that uses finger distance to adjust system volume:

* **Index fingertip (ID 8)**
* **Thumb tip (ID 4)**
* Distance between them determines volume:

  * Far apart → 🔊 Volume Up
  * Close together → 🔉 Volume Down

---

## 🛠️ Tech Stack

* **Python 3.x**
* **OpenCV** – webcam & drawing
* **MediaPipe** – hand tracking and landmarks
* **PyAutoGUI** – control system volume keys
* **Time module** – rate-limiting input

---

## 📂 Project Structure

```
HandGestureVolumeControl/
│-- gesture_volume.py
│-- README.md
│-- media/demo.mp4
```

---

## 🧠 How It Works

### 1️⃣ Capture Webcam Frame

```python
webCam = cv2.VideoCapture(0)
```

### 2️⃣ Detect Hands using MediaPipe

```python
output = my_hands.process(rgb_image)
hands = output.multi_hand_landmarks
```

### 3️⃣ Track Index Finger (ID 8) & Thumb (ID 4)

```python
if id == 8:  # index finger tip
if id == 4:  # thumb tip
```

### 4️⃣ Compute Distance

```python
dist = ((x2-x1)**2 + (y2-y1)**2)**0.5
```

### 5️⃣ Control Volume

```python
if dist > 120:
    pyautogui.press("volumeUp")
elif dist < 60:
    pyautogui.press("volumeDown")
```

---

## 📦 Installation

### 1️⃣ Install Dependencies

```bash
pip install opencv-python mediapipe pyautogui
```

### 2️⃣ Run the Script

```bash
python gesture_volume.py
```

### 3️⃣ Controls

| Action       | Gesture                  |
| ------------ | ------------------------ |
| Volume Up    | Increase finger distance |
| Volume Down  | Decrease finger distance |
| Exit Program | Press **Esc** key        |

---

## 🛡️ Requirements

* A working webcam
* Python 3.8+
* MediaPipe supports CPU execution
* Windows/macOS/Linux supported

---

## 🎯 Features

* No physical controller needed
* Smooth finger tracking
* Real-time processing
* Works on any system
* Lightweight and simple

---

## ⚠️ Troubleshooting

### Webcam not opening?

Try changing the camera index:

```python
cv2.VideoCapture(1)
```

### Volume not changing?

Run Python as **administrator** (Windows).
PyAutoGUI needs key press permissions.

---

## 🤝 Contributing

Pull requests and improvements are welcome.

---

## 📜 License

MIT License
