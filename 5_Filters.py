import cv2
import numpy as np

image1 = cv2.imread('D:\DHARUN\STUDY\SEM 5\Research\Dicom Sample\hand-x-ray-768x923.jpg')
img=cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
kernel = np.identity(5)
img1 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
conv = cv2.filter2D(src=img, ddepth=-1, kernel=kernel)
blur = cv2.GaussianBlur(img, (11, 11), 0)
bilateral_filter = cv2.bilateralFilter(src=img, d=9, sigmaColor=75, sigmaSpace=75)
median = cv2.medianBlur(src=img1, ksize=3)
#canny1 = cv2.Canny(blur, 30, 150, 3)
#canny2 = cv2.Canny(bilateral_filter, 30, 150, 3)
#canny3 = cv2.Canny(median, 30, 150, 3)

cv2.imshow('conv_ones',conv)
cv2.imshow('GaussianBlur',blur)
cv2.imshow('BilateralBlur',bilateral_filter)
cv2.imshow('MedianBlur',median)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
