import cv2 as cv
import random

def showImg(img):
    cv.imshow('image', img)
    cv.waitKey(500)
    cv.destroyAllWindows()

def getContornos(folder, nome):
    
    img = cv.imread(nome)
    copy = img.copy()
    imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    ret, thresh = cv.threshold(imgray, 200, 255, 0)
    contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

    cont = 0
    for i in range(2,len(contours)): 
        if(cv.contourArea(contours[i]) > 1.0):
            print('Contorno {}... Area: {}'.format(i,cv.contourArea(contours[i])))

            cv.fillPoly(copy, pts = [contours[i]], color=(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)))
            '''
            # faz um bound box do contorno identificado
            x,y,w,h = cv.boundingRect(contours[i])
            ROI = img[y:y+h, x:x+w]

            
            cv.rectangle(copy,(x,y),(x+w,y+h),(0,0,255),2)
            '''
            cv.imwrite(folder+nome,copy)
            showImg(copy)

            cont += 1

def main():
    getContornos('imagens/', 'mapa.jpg')

main()

 