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

def thread(i, imgs):
    t1 = threading.Thread(target=detect, args=(imgs[0], i + 1))
    t2 = threading.Thread(target=detect, args=(imgs[1], i + 2))
    t3 = threading.Thread(target=detect, args=(imgs[2], i + 3))
    t4 = threading.Thread(target=detect, args=(imgs[3], i + 4))
    t5 = threading.Thread(target=detect, args=(imgs[4], i + 5))
    t6 = threading.Thread(target=detect, args=(imgs[5], i + 6))
    t7 = threading.Thread(target=detect, args=(imgs[6], i + 7))
    t8 = threading.Thread(target=detect, args=(imgs[7], i + 8))
    t9 = threading.Thread(target=detect, args=(imgs[8], i + 9))
    t10 = threading.Thread(target=detect, args=(imgs[9], i + 10))
    t11 = threading.Thread(target=detect, args=(imgs[10], i + 11))
    t12 = threading.Thread(target=detect, args=(imgs[11], i + 12))
    t13 = threading.Thread(target=detect, args=(imgs[12], i + 13))
    t14 = threading.Thread(target=detect, args=(imgs[13], i + 14))
    t15 = threading.Thread(target=detect, args=(imgs[14], i + 15))
    t16 = threading.Thread(target=detect, args=(imgs[15], i + 16))
    t17 = threading.Thread(target=detect, args=(imgs[16], i + 17))
    t18 = threading.Thread(target=detect, args=(imgs[17], i + 18))
    t19 = threading.Thread(target=detect, args=(imgs[18], i + 19))
    t20 = threading.Thread(target=detect, args=(imgs[19], i + 20))
    t21 = threading.Thread(target=detect, args=(imgs[20], i + 21))
    t22 = threading.Thread(target=detect, args=(imgs[21], i + 22))
    t23 = threading.Thread(target=detect, args=(imgs[22], i + 23))
    t24 = threading.Thread(target=detect, args=(imgs[23], i + 24))
    t25 = threading.Thread(target=detect, args=(imgs[24], i + 25))
    t26 = threading.Thread(target=detect, args=(imgs[25], i + 26))
    t27 = threading.Thread(target=detect, args=(imgs[26], i + 27))
    t28 = threading.Thread(target=detect, args=(imgs[27], i + 28))
    t29 = threading.Thread(target=detect, args=(imgs[28], i + 29))
    t30 = threading.Thread(target=detect, args=(imgs[29], i + 30))
    t31 = threading.Thread(target=detect, args=(imgs[30], i + 31))
    t32 = threading.Thread(target=detect, args=(imgs[31], i + 32))
    t33 = threading.Thread(target=detect, args=(imgs[32], i + 33))
    t34 = threading.Thread(target=detect, args=(imgs[33], i + 34))
    t35 = threading.Thread(target=detect, args=(imgs[34], i + 35))
    t36 = threading.Thread(target=detect, args=(imgs[35], i + 36))
    t37 = threading.Thread(target=detect, args=(imgs[36], i + 37))
    t38 = threading.Thread(target=detect, args=(imgs[37], i + 38))
    t39 = threading.Thread(target=detect, args=(imgs[38], i + 39))
    t40 = threading.Thread(target=detect, args=(imgs[39], i + 40))
    t41 = threading.Thread(target=detect, args=(imgs[40], i + 41))
    t42 = threading.Thread(target=detect, args=(imgs[41], i + 42))
    t43 = threading.Thread(target=detect, args=(imgs[42], i + 43))
    t44 = threading.Thread(target=detect, args=(imgs[43], i + 44))
    t45 = threading.Thread(target=detect, args=(imgs[44], i + 45))
    t46 = threading.Thread(target=detect, args=(imgs[45], i + 46))
    t47 = threading.Thread(target=detect, args=(imgs[46], i + 47))
    t48 = threading.Thread(target=detect, args=(imgs[47], i + 48))
    t49 = threading.Thread(target=detect, args=(imgs[48], i + 49))
    t50 = threading.Thread(target=detect, args=(imgs[49], i + 50))
    t51 = threading.Thread(target=detect, args=(imgs[50], i + 51))
    t52 = threading.Thread(target=detect, args=(imgs[51], i + 52))
    t53 = threading.Thread(target=detect, args=(imgs[52], i + 53))
    t54 = threading.Thread(target=detect, args=(imgs[53], i + 54))
    t55 = threading.Thread(target=detect, args=(imgs[54], i + 55))
    t56 = threading.Thread(target=detect, args=(imgs[55], i + 56))
    t57 = threading.Thread(target=detect, args=(imgs[56], i + 57))
    t58 = threading.Thread(target=detect, args=(imgs[57], i + 58))
    t59 = threading.Thread(target=detect, args=(imgs[58], i + 59))
    t60 = threading.Thread(target=detect, args=(imgs[59], i + 60))

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
    t25.start()
    t26.start()
    t27.start()
    t28.start()
    t29.start()
    t30.start()
    t31.start()
    t32.start()
    t33.start()
    t34.start()
    t35.start()
    t36.start()
    t37.start()
    t38.start()
    t39.start()
    t40.start()
    t41.start()
    t42.start()
    t43.start()
    t44.start()
    t45.start()
    t46.start()
    t47.start()
    t48.start()
    t49.start()
    t50.start()
    t51.start()
    t52.start()
    t53.start()
    t54.start()
    t55.start()
    t56.start()
    t57.start()
    t58.start()
    t59.start()
    t60.start()

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
    t25.join()
    t26.join()
    t27.join()
    t28.join()
    t29.join()
    t30.join()
    t31.join()
    t32.join()
    t33.join()
    t34.join()
    t35.join()
    t36.join()
    t37.join()
    t38.join()
    t39.join()
    t40.join()
    t41.join()
    t42.join()
    t43.join()
    t44.join()
    t45.join()
    t46.join()
    t47.join()
    t48.join()
    t49.join()
    t50.join()
    t51.join()
    t52.join()
    t53.join()
    t54.join()
    t55.join()
    t56.join()
    t57.join()
    t58.join()
    t59.join()
    t60.join()

# Loading the video into python
cap = cv2.VideoCapture('bunny.mp4')

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
        if(len(imgs) != 0):
            for i in range(len(imgs)):
                detect(img[i], currentFrame)
        break

    # Converting the frame to grayscale and adding it to a list
    name = './data/frame' + str(currentFrame) + '.jpg'
    print ('Slicing and converting to grayscale...' + name)

    imgs.append(rgb2gray(frame))

    if(currentFrame % 60 == 0 and currentFrame != 0):
        thread((currentFrame / 60) - 1, imgs)
        imgs = []

    # Find height and width
    height, width, _ = frame.shape

    currentFrame += 1

image_folder = 'data'

images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, _ = frame.shape

exportVid()

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()