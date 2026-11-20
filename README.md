# Face Landmark Tracking with MediaPipe

Webcam-based OpenCV/MediaPipe face mesh demo showing estimated eyes open/closed, mouth open/closed and head roll angle.

## Run
```bash
python -m pip install -r requirements.txt
python detector.py
```

Press Q to quit. Requires a webcam and a Python/MediaPipe-compatible operating system.

- `detector.py`: executable script
- `requirements.txt`: dependencies

The eye/mouth thresholds are simple heuristics and may be inaccurate. This is not identity recognition, medical analysis or a validated fatigue detector.

Author: Mohsin Atta
