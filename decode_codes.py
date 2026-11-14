from PIL import Image
from pyzbar.pyzbar import decode

IMAGE_FILES = ["qr_code.png", "barcode.png"]

def main():
    for image_file in IMAGE_FILES:
        print(f"\n{image_file}:")
        results = decode(Image.open(image_file))
        
        if not results:
            print(" No QR code or barcode found")
            continue
            
        for result in results:
            print(f" Type: {result.type}")
            print(f" Data: {result.data.decode('utf-8')}")

if __name__ == "__main__":
    main()