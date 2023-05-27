
import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog

# Function to open file dialog and get video file path
def get_video_path():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4")])
    return file_path
  
  # Get video file path from user
video_path = get_video_path()

# Check if a valid video file path is selected
if not video_path:
    print("No video file selected.")
    exit()
    
  # Read video file
cap = cv2.VideoCapture(video_path)  

while True:
     read_ok, img = cap.red()
     img_bcp = img.copy()
     
     img = cv2.resize(img, (640, 480))
     # Make a copy to draw contour outline
     input_image_cpy = img.copy()   
     
     hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

     # define range of red color in HSV
     lower_red = np.array([0, 50, 50])
     upper_red = np.array([10, 255, 255])

    # define range of green color in HSV
     lower_green = np.array([40, 20, 50])
     upper_green = np.array([90, 255, 255])
      

    # define range of blue color in HSV
     lower_blue = np.array([100, 50, 50])
     upper_blue = np.array([130, 255, 255]) 
      
    # define range of yellow color in HSV
     lower_yellow = np.array([20, 100, 100])
     upper_yellow = np.array([30, 255, 255])

     # define range of orange color in HSV
     lower_orange = np.array([10, 100, 20])
     upper_orange = np.array([25, 255, 255]
     
     # create a mask for red color
      mask_red = cv2.inRange(hsv, lower_red, upper_red)
       # create a mask for green color
      mask_green = cv2.inRange(hsv, lower_green, upper_green)
       # create a mask for blue color
      mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
      # create a mask for yellow color
      mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)
      # create a mask for orange color
      mask_orange = cv2.inRange(hsv, lower_orange, upper_orange)
      
      # find contours in the red mask
     contours_red, _ = cv2.findContours(mask_red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
      # find contours in the green mask
     contours_green, _ = cv2.findContours(mask_green, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
      # find contours in the blue mask
     contours_blue, _ = cv2.findContours(mask_blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
     # find contours in the yellow mask
     contours_yellow, _ = cv2.findContours(mask_yellow, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
      # find contours in the orange mask
     contours_orange, _ = cv2.findContours(mask_orange, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
     
      # loop through the red contours and draw a rectangle around them
      for cnt in contours_red:
        contour_area = cv2.contourArea(cnt)
        if contour_area > 1000:
               x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(img, 'Red', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
            
         # loop through the green contours and draw a rectangle around them   
        for cnt in contours_green:
        contour_area = cv2.contourArea(cnt)
        if contour_area > 1000:    
              x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(img, 'Green', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
            
           # loop through the blue contours and draw a rectangle around them  
             for cnt in contours_blue:
        contour_area = cv2.contourArea(cnt)
        if contour_area > 1000:
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(img, 'Blue', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
            
         # loop through the yellow contours and draw a rectangle around them    
          for cnt in contours_yellow:
        contour_area = cv2.contourArea(cnt)
        if contour_area > 1000:
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)
            cv2.putText(img, 'Yellow', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 255), 2)   
            
          # loop through the orange contours and draw a rectangle around them   
            for cnt in contours_orange:
        contour_area = cv2.contourArea(cnt)
        if contour_area > 1000:
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 165, 255), 2)
            cv2.putText(img, 'Orange', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 165, 255), 2) 
            
            cv2.imshow('Color Recognition Output', img)
     
    # Close video window by pressing 'x'
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
   
            
