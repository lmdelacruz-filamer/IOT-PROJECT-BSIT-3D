import os
import platform
import cv2
import numpy as np

WIDTH, HEIGHT, = 800, 600
if platform.system() == "Linux":
    os.environ["QT_QPA_PLATFORM"] = "xcb"
    os.environ["QT_QPA_FONTDIR"] = "/usr/share/fonts" # silence "Cannot find font directory" warning

def polygon(center, radius, sides, rotation=-90):
    cx, cy = center
    angles = np.radians(rotation + np.arange(sides) * 360 / sides)
    return np.stack([cx + radius * np.cos(angles), cy + radius * np.sin(angles)], axis=1).astype(np.int32)

def main():

    # white canvas, BGR
    image = np.full((HEIGHT, WIDTH, 3), 255, dtype=np.uint8)

    cv2.circle(image, (150, 120), 70, (0, 120, 220), -1) # orange circle
    cv2.fillPoly(image, [polygon((400, 140), 70, 5)], (0, 150, 150)) # olive pentagon
    cv2.fillPoly(image, [polygon((650, 130), 70, 6, 0)], (180, 0, 179)) # magenta hexagon
    cv2.fillPoly(image, [np.array([[150, 300], [220, 450], [80, 450]])], (0, 0, 200)) # red traingle
    cv2.rectangle(image, (300, 300), (420, 420), (0, 180, 1), -1) # green square
    cv2.rectangle(image, (520, 320), (740, 430), (200, 0, 1), -1) # blue triangle

    while True:
        cv2.imshow("Generated", image)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    file_location = "shapes.jpg"
    print(f"Saved Generated image to '{file_location}'")
    cv2.imwrite(file_location, image)

if __name__ == "__main__":
    main()