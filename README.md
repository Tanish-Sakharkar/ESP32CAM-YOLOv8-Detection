# ESP32-CAM Object Detection with YOLOv8

Real-time object detection stream using an ESP32-CAM, OpenCV, and YOLOv8.

---

## Prerequisites

* Python 3.8+
* ESP32-CAM connected to the same Wi-Fi network as your PC

---

## Installation

https://github.com/Tanish-Sakharkar/ESP32CAM-YOLOv8-Detection/blob/main/detect.py
 
   Install required dependencies:
   pip install opencv-python ultralytics

   Usage
   1 . Open main.py and replace the stream URL with your ESP32-CAM IP:
   url = 'http://<YOUR_ESP32_IP>:81/stream'
   
   2.  Run the detection script:
    python main.py
