import sys
import cv2

def elongation(m):
    x = m['mu20'] + m['mu02']
    y = 4 * m['mu11']**2 + (m['mu20'] - m['mu02'])**2
    return (x + y**0.5) / (x - y**0.5)

image1 = cv2.imread('D:\DHARUN\STUDY\SEM 5\Research\Dicom Sample\hand-x-ray-768x923.jpg')
 
img=cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)

img = 255 - cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)[1]

m = cv2.moments(img)
print(elongation(m))