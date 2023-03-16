import cv2
import numpy as np
import os
from os.path import isfile, join
import sys

# Function for converting an image to grayscale
def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])

# Export of video
def exportVid(exportLoc, fps):
    frame_array = []
    files = [f for f in os.listdir('data/') if isfile(join('data/', f))]
 
    files.sort(key = lambda x: int(x[5:-4]))

    filename = 'data/' + files[0]
    img = cv2.imread(filename)
    height, width, _ = img.shape
    size = (width, height)

    fourcc = cv2.VideoWriter_fourcc(*'DIVX')
    out = cv2.VideoWriter(exportLoc, fourcc, fps, (width, height))
 
    for i in range(len(files)):
        filename = 'data/' + files[i]
        img = cv2.imread(filename)
        out.write(img)
 
    out.release()
    sys.exit()