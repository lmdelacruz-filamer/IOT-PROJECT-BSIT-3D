import cv2
import mediapipe as mp

CAM_SOURCE = 1 # laptop webcam. Lab PC + phone: "http://localhost:8080/video"


def main():
    mp_face_detection = mp.solutions.face_detection

    if isinstance(CAM_SOURCE, int):
        cap = cv2.VideoCapture(CAM_SOURCE, cv2.CAP_DSHOW)
        if not cap.isOpened():
            cap = cv2.VideoCapture(CAM_SOURCE)
    else:
        cap =  cv2.VideoCapture(CAM_SOURCE)
    if not cap.isOpened():
        raise RuntimeError("Could not open webcam. Check CAM_SOURCE / camera permissions.")

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    print("AR Face Tracker runnin. Press 'q' to quit.")

    with mp_face_detection.FaceDetection(
        model_selection=0, min_detection_confidence=0.6
    ) as face_detection:
        
        while True:
            ok, frame = cap.read()
            if not ok:
                break

            frame = cv2.flip(frame, 1)
            h, w = frame.shape[:2]
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            rgb.flags.writeable = False

            det_results = face_detection.process(rgb)

            if det_results.detections:
                for det in det_results.detections:
                    box = det.location_data.relative_bounding_box
                    x1 = max(0, int(box.xmin * w) - 15)
                    y1 = max(0, int(box.ymin * h) - 15)
                    x2 = min(w, int((box.xmin + box.width) * w) + 15)
                    y2 = min(h, int((box.ymin + box.height) * h) + 15)
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    
            cv2.imshow("AR Face Tracker", frame)
            key = cv2.waitKey(1) & 0xFF
            if key in (ord("q"), 27):
                break

    cap.release()
    cv2.destroyAllWindows()       


if __name__ == "__main__":
    main()