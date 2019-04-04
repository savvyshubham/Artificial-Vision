import cv2
import time
import matplotlib.pyplot as plt
cap = cv2.VideoCapture(0)
sif cap.isOpened():
    ifcap,frame = cap.read() 
#    cap.release()
#    if ifcap and frame is not None:
#        plt.imshow(frame)
#        cv2.imwrite('img.jpg', frame)