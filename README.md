# ASCII Video Player
A terminal-based video renderer that converts video frames into animated ASCII art using Python.
The program processes each frame of a video file using OpenCV and maps pixel brightness values to ASCII characters to recreate the video in text form directly inside the terminal.
This project explores real-time frame processing, image manipulation, and creative terminal rendering techniques.

#Live Demo
Run locally to see the ASCII animation in your terminal.
``` ```python ascii_video.py

Or run with a custom video file:
python ascii_video.py your_video.mp4

## Key Features
- Converts video frames into ASCII art in real time
- Terminal-based animation playback
- Lightweight script with minimal dependencies

## Tech Stack
Python, OpenCV, NumPy

## How It Works
1. The program loads a video file using OpenCV.
2. Each frame is converted to grayscale.
3. The frame is resized to a manageable resolution for terminal display.
4. Pixel brightness values are mapped to ASCII characters representing different intensity levels.
5. The ASCII frame is printed to the terminal, creating a text-based animation.

## Project Context
This project was developed as an experimental exploration of creative programming and computer vision techniques.
It focuses on understanding how image data can be transformed and represented in alternative visual formats using ASCII characters, while also demonstrating real-time frame processing within a terminal environment.

## Setup
Install dependencies:
``` ```pip install -r requirements.txt

Run the project:
``` ```python ascii_video.py

Optional parameters:
``` ```python ascii_video.py sample_video.mov --width 80 --fps 20

## Notes
This project is intended as a creative programming experiment demonstrating how video data can be transformed into ASCII-based visualizations using simple computer vision techniques.
