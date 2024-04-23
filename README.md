# Car Number Plate Detection Project

This project is an implementation of car number plate detection using OpenCV and Haar cascade classifiers. The objective is to detect the number plates of cars from video feeds or images and highlight them with bounding boxes.

## Overview
The project uses the OpenCV library to capture video frames and applies the Haar cascade classifier to detect car number plates. The results are then displayed with rectangles drawn around detected number plates. This approach is useful for simple vehicle identification tasks.

## Implementation Details
- **Language/Framework**: Python with OpenCV.
- **Detection Algorithm**: Haar cascade classifier.
- **Parameters**:
  - `scaleFactor`: 1.2
  - `minNeighbours`: 5
- **Preprocessing**: Conversion to grayscale for efficient processing.

## How to Use
1) Clone the repository.
2) Install the required packages:
   ```bash
   conda install -c conda-forge opencv
3) Run the script to start video capture and detect number plates:
   ```
   python detect_number_plate.py
4) Adjust parameters (e.g., scaleFactor, minNeighbours) to improve detection accuracy if needed.
