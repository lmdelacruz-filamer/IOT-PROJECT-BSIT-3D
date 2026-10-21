import cv2

INPUT = """ print( helllo , world )"""
OUTPUT_FILE = "qr_code.png"
SCALE = 15  # pixels per QR module


def generate_qr(text: str):
    params = cv2.QRCodeEncoder_Params()
    params.correction_level = cv2.QRCodeEncoder_CORRECT_LEVEL_M

    encoder = cv2.QRCodeEncoder_create(params)
    qr_image = encoder.encode(text)

    qr_image = cv2.copyMakeBorder(
        qr_image, 2, 2, 2, 2, cv2.BORDER_CONSTANT, value=255
    )

    return cv2.resize(
        qr_image,
        (qr_image.shape[1] * SCALE, qr_image.shape[0] * SCALE),
        interpolation=cv2.INTER_NEAREST,
    )


def main():
    running = True
    image = generate_qr(INPUT)

    while running:
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            running = False

        cv2.imshow("QR code Sample", image)

    if not cv2.imwrite(OUTPUT_FILE, image):
        raise SystemExit(f"Could not write image to {OUTPUT_FILE}")

    print(f"QR code for {LINK} saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()