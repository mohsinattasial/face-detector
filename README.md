Face, Eye, Mouth, and Head Tracking using MediaPipe

This Python project uses MediaPipe Face Mesh and OpenCV to detect face landmarks in real-time and monitor:

Eye status (open/closed) using Eye Aspect Ratio (EAR)

Mouth status (open/closed) using Mouth Aspect Ratio (MAR)

Head tilt (roll) angle

Features:

Real-time face mesh overlay

Detects and displays eye open/closed status

Detects and displays mouth open/closed status

Calculates head roll angle for head tilt monitoring

Works with a single webcam

Technologies Used:

Python 3

OpenCV

MediaPipe (Face Mesh)

NumPy & Math modules

Project Structure:
Face_Tracking/
├── face_tracking.py # Main script
└── README.txt

How to Run:

Make sure Python 3 is installed.

Install required packages:
pip install opencv-python mediapipe

Run the script:
python face_tracking.py

A window will open showing the webcam feed.

Eyes, mouth, and head roll status will be displayed in real-time.

Press 'q' to quit.

How It Works:

MediaPipe Face Mesh detects 468 facial landmarks.

Eye Aspect Ratio (EAR) calculates eye open/closed status.

Mouth Aspect Ratio (MAR) calculates mouth open/closed status.

Head roll angle is calculated using positions of left and right eyes.

OpenCV overlays status text and face mesh on the video feed.

Purpose:

Demonstrate real-time facial feature tracking using computer vision

Practice MediaPipe Face Mesh and OpenCV integration

Build interactive AI applications for attention, drowsiness, or expression monitoring

Future Improvements:

Detect multiple faces simultaneously

Log status for analytics (drowsiness, yawns, etc.)

Integrate with alerts or notifications

Add blink detection or yawn count

Author: Mohsin Atta
