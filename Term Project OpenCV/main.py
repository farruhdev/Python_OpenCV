
import cv2
import numpy as np


cap = cv2.VideoCapture('C:/')

while True:
     read_ok, img = cap.red()
     img_bcp = img.copy()
     
     img = cv2.resize(img, (640, 480))
     input_image_cpy = img.copy()   
     
     hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

     lower_red = np.array([0, 50, 50])
      upper_red = np.array([10, 250, 250])

      lower_green = np.array([40, 25, 55])
      upper_green = np.array([90, 255, 255])

      lower_blue = np.array([100, 55, 55])
      upper_blue = np.array([130, 250, 255]) 
      
      lower_yellow = np.array([20, 100, 100])
      upper_yellow = np.array([30, 250, 250])

    
     lower_orange = np.array([11, 50, 50])
     upper_orange = np.array([25, 250, 250]
     
    
   
   
            
