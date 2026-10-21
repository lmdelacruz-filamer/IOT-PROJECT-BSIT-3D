import os
import platform
import cv2
import numpy as np

if platform.system() == "Linux":
    os.environ["QT_QPA_PLATFORM"] = "xcb"
    os.environ["QT_QPA_FONTDIR"] = "/usr/share/fonts"


def main():
    folder = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(folder, "shapes.jpg")

    image = cv2.imread(image_path)

    if image is None:
        print("Error: shapes.jpg is missing or unreadable.")
        print("Run activity_6.py first.")
        print(f"Expected image location: {image_path}")
        return

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 30, 100)
    overlay = image.copy()

    lines = cv2.HoughLinesP(
        edges, 1, np.pi / 180, 45,
        minLineLength=50, maxLineGap=5
    )

    circles = cv2.HoughCircles(
        gray, cv2.HOUGH_GRADIENT,
        dp=1.2, minDist=50,
        param1=100, param2=30,
        minRadius=10, maxRadius=200
    )

    if lines is not None:
        for x1, y1, x2, y2 in lines.reshape(-1, 4):
            cv2.line(overlay, (x1, y1), (x2, y2), (255, 0, 255), 2)

    if circles is not None:
        for x, y, r in np.round(circles[0]).astype(int):
            cv2.circle(overlay, (x, y), r, (255, 0, 255), 2)

    cv2.imshow("Edges", overlay)
    print("Detection complete. Press Q to close.")

    while True:
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()