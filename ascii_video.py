import cv2
import numpy as np
import time
import argparse

ASCII_CHARS = "@%#*+=-:. "

def frame_to_ascii(frame, width=60):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    height, original_width = gray.shape
    aspect_ratio = height / original_width
    new_height = int(width * aspect_ratio * 0.55)

    resized = cv2.resize(gray, (width, new_height))

    ascii_frame = ""
    for row in resized:
        for pixel in row:
            ascii_frame += ASCII_CHARS[int(pixel) * len(ASCII_CHARS) // 256]
        ascii_frame += "\n"

    return ascii_frame


parser = argparse.ArgumentParser(description="Convert video to ASCII animation in the terminal")

# Video argument is now OPTIONAL
parser.add_argument(
    "video",
    nargs="?",
    default="sample_video.mov",
    help="Path to video file (default: sample_video.mov)"
)

parser.add_argument("--width", type=int, default=60, help="ASCII output width")
parser.add_argument("--fps", type=int, default=30, help="Playback FPS")

args = parser.parse_args()

video = cv2.VideoCapture(args.video)

if not video.isOpened():
    print(f"Error: Could not open video file '{args.video}'")
    exit()

while True:
    ret, frame = video.read()
    if not ret:
        break

    # Clear terminal
    print("\033[H\033[J", end="")

    print(frame_to_ascii(frame, args.width))

    time.sleep(1 / args.fps)

video.release()