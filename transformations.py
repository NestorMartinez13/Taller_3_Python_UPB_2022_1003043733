import cv2 as cv
import numpy as np

img1 = cv.imread("imagenes/img1.jpg")
img2 = cv.imread("imagenes/img2.png")
cv.imwrite("Resultados/Original_Universe.png", img1)
cv.imwrite("Resultados/Original_Thanos.png", img2)


#####################################################################
def rescale(image, scale=0.5):
    width = int(image.shape[1]*scale)
    height = int(image.shape[0]*scale)
    dimensions = (width, height)

    return cv.resize(image, dimensions, interpolation=cv.INTER_AREA)

img1_rescale = rescale(img1)
img2_rescale = rescale(img2)
cv.imwrite("Resultados/Rescaled_Universe.png",img1_rescale)
cv.imwrite("Resultados/Rescaled_Thanos.png",img2_rescale)

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
    cv.putText(image2, "I AM INEVIBALE", (230, 480), cv.FONT_HERSHEY_DUPLEX, 1, (255, 255, 255),  2)

    
    return(image2)

draw11 = draws1(img1)
draw12 = draws2(img2)
cv.imwrite("Resultados/Draw_Universe.png", draw11 )
cv.imwrite("Resultados/Draw_Thanos.png", draw12)


####################################################################
def ColorScale(image):
    con = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    return(con) 

def grayScale(image):
    con = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    return(con)

con_uni = ColorScale(img1)
con_tha = ColorScale(img2)
gray_uni = grayScale(img1)
gray_tha = grayScale(img2)

cv.imwrite("Resultados/Inverted_Universe.png", con_uni)
cv.imwrite("Resultados/Iverted_Thanos.png", con_tha)
cv.imwrite("Resultados/Gray_Universe.png", gray_uni)
cv.imwrite("Resultados/Gray_Thanos.png", gray_tha)
######################################################################

#recro = cv.rectangle(img1, (575, 320), (477, 220), (0,0,255), thickness=2)
def croped1():
    UniCro = img1[220:320, 477:575]
    return(UniCro)

#recro = cv.rectangle(img2, (230, 10), (400, 225), (0, 0, 255), thickness=2)
def croped2():
    ThaCro = img2[10:225, 230:400]
    return(ThaCro)

CropUni =croped1() 
CropTha =croped2()

cv.imwrite("Resultados/Croped_Star.png", CropUni)
cv.imwrite("Resultados/Croped_Thanos.png", CropTha)
######################################################################
def th(img):
    ret, thresh = cv.threshold(img, 110, 255, cv.THRESH_BINARY)
    return(thresh)

thresh_uni= th(gray_uni)
thresh_tha = th(gray_tha)

cv.imwrite("Resultados/Thresh_Thanos.png", thresh_tha)
cv.imwrite("Thresh_Universe.png", thresh_uni)

#######################################################################
def mask(image):
    blank = np.zeros(image.shape[:2], dtype = "uint8")
    circle = cv.circle(blank, (image.shape[1]//2,image.shape[0]//2),100,255, -1)
    masked = cv.bitwise_and(image,image,mask=circle)
    return(masked)

masked_uni = mask(img1)
masked_Thanos = mask(img2)
cv.imwrite("Resultados/Masked_Uni.png", masked_uni)
cv.imwrite("Resultados/Masked_Thanos.png", masked_Thanos)

########################################################################


