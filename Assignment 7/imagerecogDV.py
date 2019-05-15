import cv2
import numpy as numpy
import matplotlib.pyplot as plt

def detect_faces(cascade, test_image, scaleFactor):
    
    image_copy = test_image.copy()
   
    gray_image = cv2.cvtColor(image_copy, cv2.COLOR_BGR2GRAY)
    
    face = cascade.detectMultiScale(gray_image, scaleFactor=scaleFactor, minNeighbors=4)

    for (x, y, w, h) in face:
        cv2.rectangle(image_copy, (x, y), (x+w, y+h), (0, 255, 0), 4)

    return image_copy

img = cv2.imread("60\\16BIT060_Male_Happy_RGB.jpeg",1)
img=cv2.resize(img,(int(img.shape[1]/6),int(img.shape[0]/6)))

haar_cascade_face = cv2.CascadeClassifier('C:\\Users\\Patel\\Anaconda3\\envs\\opencv-env\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml')
detected_img = detect_faces(haar_cascade_face,img,1.3)

cv2.imshow("Legend",detected_img)
cv2.waitKey(0)