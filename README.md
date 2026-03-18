# Face Mask Detection System

A real-time face mask detection system built using Deep Learning (MobileNetV2)
and OpenCV. Detects whether a person is wearing a face mask or not via webcam
feed and displays a color-coded bounding box.

## What It Does
- Green box = Mask worn ✅
- Red box = No mask ❌
- Shows confidence percentage in real time

## Tech Stack
- Python
- TensorFlow / Keras (MobileNetV2)
- OpenCV
- imutils

## How to Run

### 1. Install dependencies
pip install tensorflow opencv-python imutils numpy

### 2. Test your webcam
python test.py

### 3. Run mask detector
python Face.py
