import cv2
import numpy as np
import os
from canny_edge import *
import threading
from utils import *

def mainFunc(sourceLoc, destLoc):
    # Loading the video into python
    cap = cv2.VideoCapture(sourceLoc)

    # Making a folder for the edited frames
    try:
        if not os.path.exists('data'):
            os.makedirs('data')
    except OSError:
        print('Error: Creating directory of data')

    currentFrame = 1
    imgs = []
    height = 0
    width = 0
    n = 0

    # Determining the FPS of the given video
    fps = cap.get(cv2.CAP_PROP_FPS)

    nThreads = 60
    while(True):
        # Capture frame by frame
        ret, frame = cap.read()

        if not ret:
            if(len(imgs) != 0):
                for i in range(len(imgs)):
                    cannyDetect(imgs[i], currentFrame)
            break

        # Converting the frame to grayscale and adding it to a list
        print('Slicing and converting to grayscale frame ' + str(currentFrame))
        imgs.append(rgb2gray(frame))

        threadList = []

        # Starting threading on the last 60 frames
        if(currentFrame % nThreads == 0 and currentFrame != 0):
            print('Starting Canny Edge Detection on ' + str(currentFrame - nThreads + 1) + ' - ' + str(currentFrame))
            for i in range(1, nThreads + 1):
                threadList.append(threading.Thread(target=cannyDetect, args=(imgs[i-1], currentFrame - (nThreads - i))))

            for i in range(nThreads):
                threadList[i].start()

            for i in range(nThreads):
                threadList[i].join()
            
            imgs = []
            threadList = []

        currentFrame += 1

    print(str('Exporting ' + destLoc))
    exportVid(destLoc, fps)

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
