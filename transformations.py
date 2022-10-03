import cv2 as cv
import numpy as np
img1 = cv.imread("imagenes/img1.jpg")
img2 = cv.imread("imagenes/img2.png")
# cv.imshow("Universe original", img1)
# cv.imshow("Thanos", img2)

#####################################################################
def rescale(image, scale=0.5):
    width = int(image.shape[1]*scale)
    height = int(image.shape[0]*scale)
    dimensions = (width, height)

    return cv.resize(image, dimensions, interpolation=cv.INTER_AREA)

img1_rescale = rescale(img1)
img2_rescale = rescale(img2)
#cv.imshow("rescaled Universe",img1_rescale)
#cv.imshow("rescaled Thanos",img2_rescale)
####################################################################

def draws1 (image1):
    
    cv.rectangle(image1, (500, 100), (50, 20), (43, 54, 165), thickness=2)
    cv.circle(image1, (530, 60), 50, (255, 64, 255), thickness=-1)
    cv.circle(image1, (500, 200), 80, (112, 10, 30), thickness=2)
    cv.circle(image1, (100, 200), 100, (64, 87, 130), thickness=-1)
    cv.line(image1,(200,0),(600,200),(0,255,0),thickness=10)
    cv.putText(image1, "This is magnificent", (100, 200), cv.FONT_HERSHEY_TRIPLEX, 1, (255, 255, 255),  2)
    
    return(image1)

def draws2(image2):
    cv.rectangle(image2, (500, 540), (200, 400), (43, 54, 165), thickness=cv.FILLED)
    cv.circle(image2, (530, 60), 50, (120, 280, 30), thickness=-1)
    cv.circle(image2, (310, 110), 100, (12, 210, 30), thickness=2)
    cv.circle(image2, (100, 200), 100, (120, 80, 130), thickness=-1)
    cv.line(image2,(600,0),(0,600),(255,255,0),thickness=10)
    cv.putText(image2, "I AM INEVITABLE", (230, 480), cv.FONT_HERSHEY_DUPLEX, 1, (255, 255, 255),  2)

    
    return(image2)
    

img1_draw = draws1(img1)
img2_draw = draws2(img2)
# cv.imshow("draw Universe", img1_draw)
# cv.imshow("draw Thanos", img2_draw)
# cv.waitKey(0)


####################################################################








cv.waitKey(0)

