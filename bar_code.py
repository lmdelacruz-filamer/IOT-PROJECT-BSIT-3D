import barcode
import cv2
import numpy as np

BARCODE_DATA = "0123456789123"
OUTPUT_FILE = "barcode.png"

MODULE_WIDTH = 10  # pixels per bar or space
BAR_HEIGHT = 200   # pixels
QUIET_ZONE = 10    # blank modules on each side

def main():
    barcode_class = barcode.get_barcode_class("code128")
    
    barcode_image = barcode_class(BARCODE_DATA)
    pattern = barcode_image.build()[0]

    width = (len(pattern) + 2 * QUIET_ZONE) * MODULE_WIDTH
    image = np.full((BAR_HEIGHT, width, 3), 255, dtype=np.uint8)

    for i, module in enumerate(pattern):
        if module in "1G":
            x = (QUIET_ZONE + i) * MODULE_WIDTH
            cv2.rectangle(image, (x, 0), (x + MODULE_WIDTH - 1, BAR_HEIGHT - 1), (0, 0, 0), -1)

    if not cv2.imwrite(OUTPUT_FILE, image):
        raise SystemExit(f"Could not write image to {OUTPUT_FILE}")
    
    print(f"Barcode saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()