
import cv2
import numpy as np


cap = cv2.VideoCapture('C:/')

while True:
     read_ok, img = cap.red()
     img_bcp = img.copy()
     
     img = cv2.resize(img, (640, 480))
     input_image_cpy = img.copy()   
     
     hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

     # define range of red color in HSV
     lower_red = np.array([0, 50, 50])
      upper_red = np.array([10, 250, 250])

     # define range of green color in HSV
      lower_green = np.array([40, 25, 55])
      upper_green = np.array([90, 255, 255])

      # define range of blue color in HSV
      lower_blue = np.array([100, 55, 55])
      upper_blue = np.array([130, 250, 255]) 
      
     # define range of yellow color in HSV
      lower_yellow = np.array([20, 100, 100])
      upper_yellow = np.array([30, 250, 250])

     # define range of orange color in HSV
     lower_orange = np.array([11, 50, 50])
     upper_orange = np.array([25, 250, 250]
     
     
      mask_red = cv2.inRange(hsv, lower_red, upper_red)
      mask_green = cv2.inRange(hsv, lower_green, upper_green)
      mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
      mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)
      mask_orange = cv2.inRange(hsv, lower_orange, upper_orange)
      
     contours_red, _ = cv2.findContours(mask_red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
     contours_green, _ = cv2.findContours(mask_green, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
     contours_blue, _ = cv2.findContours(mask_blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
     contours_yellow, _ = cv2.findContours(mask_yellow, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
     contours_orange, _ = cv2.findContours(mask_orange, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
   
            
