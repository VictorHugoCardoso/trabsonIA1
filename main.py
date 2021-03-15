import PIL
from PIL import Image, ImageFilter
import numpy as np
import cv2 as cv
import csv
import math


def showImg(img):
    cv.imshow('image', img)
    cv.waitKey(5000)
    cv.destroyAllWindows()

# recortar as folhas
def asd(folder, nome):
    
    img = cv.imread(nome)
    copy = img.copy()
    imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    ret, thresh = cv.threshold(imgray, 200, 255, 0)
    contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

    for i in range(0,len(contours)): 
        print('Contorno {}... Area: {}'.format(i,cv.contourArea(contours[i]))) 

        # faz um bound box do contorno identificado
        x,y,w,h = cv.boundingRect(contours[i])
        ROI = img[y:y+h, x:x+w]


        cv.rectangle(copy,(x,y),(x+w,y+h),(0,0,255),2)
        cv.imwrite(folder+nome,copy)


    print('\nNúmero de contornos: {}'.format(len(contours)))

def main():
    asd('imagens/', 'mapa2.jpg')

main()

 