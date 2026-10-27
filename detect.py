import cv2
from ultralytics import YOLO

# 1. LOAD THE MODEL (It will auto-download the first time)
model = YOLO('yolov8n.pt') 

# 2. CONNECT TO THE ESP32-CAM
# Replace '192.168.1.XX' with the IP from your Serial Monitor
url = 'http://10.125.200.239:81/stream' 
cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()
    if not success:
        print("Waiting for stream...")
        continue

    # 3. RUN DETECTION
    results = model(frame, conf=0.5)

    # 4. DRAW BOXES
    for r in results:
        annotated_frame = r.plot()
        cv2.imshow("SCOE Project: YOLOv8 Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()