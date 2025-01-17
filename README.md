# Hand Tracking Project

## Description
This project implements real-time hand tracking using OpenCV and MediaPipe libraries. It can detect and track hand movements through a webcam feed, identifying key landmarks and joints on the hand. The project includes both a basic implementation and a modular version with a reusable hand tracking class.

## Features
- Real-time hand detection and tracking
- Identification of 21 hand landmarks
- FPS (Frames Per Second) display
- Support for tracking multiple hands
- Visualization of hand landmarks and connections
- Modular design for easy integration into other projects

## Prerequisites
To run this project, you need to have the following libraries installed:
```bash
pip install opencv-python
pip install mediapipe
```

## Project Structure
- `HandTracking101.py` - Basic implementation of hand tracking
- `HandTrackingModule.py` - Modular implementation with a reusable HandDetector class

## Usage

### Basic Implementation (HandTracking101.py)
Run the basic version to see hand tracking in action:
```bash
python HandTracking101.py
```

### Modular Implementation (HandTrackingModule.py)
Use the HandDetector class in your own projects:
```python
from HandTrackingModule import handDetector

# Initialize detector
detector = handDetector()

# Use in your video capture loop
success, img = cap.read()
img = detector.findHands(img)
landmarkList = detector.findPosition(img)
```

## HandDetector Class Parameters
- `mode` (bool): Whether to treat images as a video stream (False) or independent images (True)
- `maxHands` (int): Maximum number of hands to detect (default: 2)
- `detectionCon` (float): Minimum detection confidence (default: 0.5)
- `trackingCon` (float): Minimum tracking confidence (default: 0.5)

## Methods
- `findHands(img, draw=True)`: Detects and draws hand landmarks on the image
- `findPosition(img, handNo=0, draw=True)`: Returns a list of landmark positions for a specific hand

## Credits
This project was created following the tutorial by [Murtaza's Workshop - Robotics and AI](https://www.youtube.com/watch?v=NZde8Xt78Iw).

