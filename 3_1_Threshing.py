import cv2
import numpy as np
image1 = cv2.imread('D:\DHARUN\STUDY\SEM 5\Research\Dicom Sample\hand-x-ray-768x923.jpg')
img=cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
kernel = np.ones((5, 5), np.uint8)
ret, thresh1 = cv2.threshold(img, 110, 255, cv2.THRESH_BINARY)
image_sharp = cv2.filter2D(src=thresh1,ddepth=-1, kernel=kernel)
cv2.imshow('Normal Threshing', image_sharp)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
