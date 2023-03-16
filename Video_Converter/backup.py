import cv2
import numpy as np
import os
from canny_edge import *
import threading

from os.path import isfile, join

# Function for converting an image to grayscale
def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])

# Export of video
def exportVid():
    frame_array = []
    files = [f for f in os.listdir('data/') if isfile(join('data/', f))]
 
    files.sort(key = lambda x: int(x[5:-4]))
 
    for i in range(len(files)):
        filename = 'data/' + files[i]
        img = cv2.imread(filename)
        height, width, _ = img.shape
        size = (width,height)
        print(filename)
        frame_array.append(img)
 
    fourcc = cv2.VideoWriter_fourcc(*'DIVX')
    out = cv2.VideoWriter('export.avi', fourcc, 24.0, (width,height))
 
    for i in range(len(frame_array)):
        out.write(frame_array[i])
    out.release()

# Loading the video into python
cap = cv2.VideoCapture('sample.avi')

# Making a folder for the edited frames
try:
    if not os.path.exists('data'):
        os.makedirs('data')
except OSError:
    print ('Error: Creating directory of data')

currentFrame = 0
imgs = []
height = 0
width = 0
n = 0
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        break

    # Converting the frame to grayscale and adding it to a list
    name = './data/frame' + str(currentFrame) + '.jpg'
    print ('Slicing and converting to grayscale...' + name)

    imgs.append(rgb2gray(frame))

    # Find height and width
    height, width, _ = frame.shape

    currentFrame += 1

for i in range(0,len(imgs),24):
    t1 = threading.Thread(target=detect, args=(imgs[i],i+1))
    t2 = threading.Thread(target=detect, args=(imgs[i+1],i+2))
    t3 = threading.Thread(target=detect, args=(imgs[i+2],i+3))
    t4 = threading.Thread(target=detect, args=(imgs[i+3],i+4))
    t5 = threading.Thread(target=detect, args=(imgs[i+4],i+5))
    t6 = threading.Thread(target=detect, args=(imgs[i+5],i+6))
    t7 = threading.Thread(target=detect, args=(imgs[i+6],i+7))
    t8 = threading.Thread(target=detect, args=(imgs[i+7],i+8))
    t9 = threading.Thread(target=detect, args=(imgs[i+8],i+9))
    t10 = threading.Thread(target=detect, args=(imgs[i+9],i+10))
    t11 = threading.Thread(target=detect, args=(imgs[i+10],i+11))
    t12 = threading.Thread(target=detect, args=(imgs[i+11],i+12))
    t13 = threading.Thread(target=detect, args=(imgs[i+12],i+13))
    t14 = threading.Thread(target=detect, args=(imgs[i+13],i+14))
    t15 = threading.Thread(target=detect, args=(imgs[i+14],i+15))
    t16 = threading.Thread(target=detect, args=(imgs[i+15],i+16))
    t17 = threading.Thread(target=detect, args=(imgs[i+16],i+17))
    t18 = threading.Thread(target=detect, args=(imgs[i+17],i+18))
    t19 = threading.Thread(target=detect, args=(imgs[i+18],i+19))
    t20 = threading.Thread(target=detect, args=(imgs[i+19],i+20))
    t21 = threading.Thread(target=detect, args=(imgs[i+20],i+21))
    t22 = threading.Thread(target=detect, args=(imgs[i+21],i+22))
    t23 = threading.Thread(target=detect, args=(imgs[i+22],i+23))
    t24 = threading.Thread(target=detect, args=(imgs[i+23],i+24))
  
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    t9.start()
    t10.start()
    t11.start()
    t12.start()
    t13.start()
    t14.start()
    t15.start()
    t16.start()
    t17.start()
    t18.start()
    t19.start()
    t20.start()
    t21.start()
    t22.start()
    t23.start()
    t24.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    t7.join()
    t8.join()
    t9.join()
    t10.join()
    t11.join()
    t12.join()
    t13.join()
    t14.join()
    t15.join()
    t16.join()
    t17.join()
    t18.join()
    t19.join()
    t20.join()
    t21.join()
    t22.join()
    t23.join()
    t24.join()

if(len(imgs) % 24 != 0):
    for i in range((len(imgs)//24)*24+1, len(imgs)):
        detect(img[i], i)

image_folder = 'data'

images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, _ = frame.shape

exportVid()

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()