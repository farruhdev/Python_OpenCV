# Project name Color recognition and object detection

## Project 소개 
This project implements a feature using OpenCV to recognize a specific color in a video and detect objects of that color. The given code detects red, green, blue, and yellow orange objects in the given video, draws rectangles around those objects, and displays the color names.

## The main phases of the project are
1 Video file loading: Open and read the video file from the given path

2 Frame processing: Before performing color recognition and object detection on each frame, resize the frame and perform necessary preprocessing.

3 HSV conversion: Convert the BGR image to the HSV (Hue, Saturation, Value) color space.
 This allows us to define the range for each color.

4 Color range definition: Defines the color range of red, green, blue, orange and yellow as HSV values.

5 Generate Color Mask: Creates a binary mask for the corresponding colors in an image using a defined range of colors.
6 Contour Detection: Detects contours in a color mask.

7 Object detection: Calculate the area of the outline, draw a rectangle for objects over a certain size and display color names around the objects

8 Result Output: Outputs the image with color recognition and object detection applied to the screen.

9 Exit Condition: Press the 'x' key to close the video window and exit the program.

  By running this project, you can observe the real-time detection of red, green, blue,  orange, and yellow objects in videos. This can be applied to various applications. For example, it can recognize signal colors in traffic lights or perform color-based object tracking.




# Orginal video
https://github.com/farruhdev/Python_OpenCV/assets/115518263/45571c38-66a4-43ff-9c79-ceb52ae4714a


# Result Video

https://github.com/farruhdev/Python_OpenCV/assets/115518263/0ad43bf6-465d-4bb0-843c-334178b904f2








