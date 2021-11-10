import easyocr
import cv2
import matplotlib.pyplot as plt
#import pytesseract
import numpy as np 
import math

def ocr_read(img):
    reader = easyocr.Reader(['en'])
    result = reader.readtext(img)
    text = ''
    for i in range(0, len(result)):
        text += result[i][1] + ' '
##easyocr matrix kodu
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.show()
    print(f'Licence Plate: {text}')


video_path = "C:/Users/halil/Desktop/video_process/car_video.mp4"
my_video = cv2.VideoCapture(video_path)

while True:
    _, image = my_video.read()

    #corner of the license plate that we wanna get perspective
    #pt1 = left upper, pt2 = right upper, pt2 = left bottom, pt3 = right bottom 
    pt1, pt2, pt3, pt4 = [3,108], [276,15],[10,161],[273,67]
    pt1, pt2, pt3, pt4 = [3,108], [276,15],[10,161],[273,67]
    xf =  abs(pt2[0] - pt1[0])
    yf = abs(pt2[1] - pt1[1])
    width = int(math.sqrt(xf**2 + yf**2))

    x1f =  abs(pt3[1] - pt1[1])
    y1f = abs(pt3[0] - pt1[0])
    height = int(math.sqrt(x1f**2 + y1f**2))

    pts1 = np.float32([pt1, pt2, pt3, pt4])
    pts2 = np.float32([[0,0], [width,0], [0,height], [width, height]])
    matrix = cv2.getPerspectiveTransform(pts1,pts2)
    imgoutput = cv2.warpPerspective(image, matrix,(width,height))
