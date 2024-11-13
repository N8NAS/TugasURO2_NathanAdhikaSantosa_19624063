from ultralytics import YOLO # import YOLO
import cv2 as cv # import opencv2 dan disingkatkan menjadi cv

model = YOLO('yolov8n.pt') # Mengambil model yoloV8 yang khususnya untuk mendeteksi objek, dimana model ini sudah dilakukan training dengan banyak objek
results = model(source="C:/Users/Nathan A.S/Downloads/bus jakarta.jpeg", show = True, conf = 0.4, save = True)
# Menampilakn hasil dari foto yang diambil dari path OS dengan menampilkan kotak dimana objek terdeteksi dengan memberi tingkat kepercayaan yang pasti diatas 0.4

cv.waitKey(0) # Menunggu sesuatu key di pencet, apabila dipencet maka program akan selesai