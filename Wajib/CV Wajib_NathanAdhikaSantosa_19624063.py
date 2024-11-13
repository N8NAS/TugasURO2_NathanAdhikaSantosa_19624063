import cv2 as cv #import library cv2 dan disingkatkan menjadi cv
import numpy as np # import library numpy dan disingkatkan menjadi np

capture = cv.VideoCapture("C:/Users/Nathan A.S/Downloads/object_video.mp4") # mengambil file video dari path OS yang ada di device

lower_HSV = np.array([160, 50, 150]) # set batasan bawah HUE, Saturation, dan value
upper_HSV = np.array([180, 255, 255]) # set batasan atas HUE, Saturation, dan value
while True: # selama True maka akan looping terus
    isTrue, frame = capture.read() # set kondisi loop sebagai True dan set frame sebagai pembacaan video yang berupa satu frame dari video
    masked_frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV) # Untuk mask frame dengan mengubah warna dari RGB(dalam opencv, semua media akan terdeteksi sebagai BGR) menjadi HSV
    HSV = cv.inRange(masked_frame, lower_HSV, upper_HSV) # Mengubah frame yang telah dimask sehinggga hanya menampilkan warna merah sebab batasan bawah dan atas HSV
    edge = cv.Canny(HSV, 100, 1000) # Mencari batasan atau pinggiran dari sebuah objek dengan Canny edge detection
    dilate = cv.dilate(edge, None, iterations=5) # Menambahkan jumlah pixel di batasan objek
    
    ret, thresh = cv.threshold(dilate, 125,255, cv.THRESH_BINARY) # Memberi value pada setiap pixel yang didalam frame sehingga yang berwarna merah akan bernilai 1
    contours, hierarchies = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE) # Mencari Contours
    for contour in contours:
        if cv.contourArea(contour) > 200: # Mencari area contour yang lebih dari 200
            x,y,w,h = cv.boundingRect(contour) # Mencari koordinat contour

            cv.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), thickness=2) # Menggambar persegi atau persegipanjang pada frame berdasarkan koordinat yang didapatkan 
            cv.putText(frame, "Objek", (x,y-11), cv.QT_FONT_NORMAL, 0.5, (0,0,255), thickness=2) # Memberi nama untuk objek yang terdeteksi
    cv.imshow('Objek Terdeteksi', frame) # Menampilkan frame yang telah deteksi objek
    if cv.waitKey(20) & 0xFF==ord('d'): # Jika key d terpencet maka program akan berhenti
        break