import cv2
import numpy as np
from PIL import Image

d1 = cv2.imread('D:\DHARUN\STUDY\SEM 5\Research\Jpg export\est1.jpg')
switch=0
for i in range(0,len(d1)-1):
  for j in range(0,len(d1[0])-1):
    if(d1[i][j]<50):
      d1[i][j]==255
      if(switch==1):
        #for k in range(0,3):
         #  d1[i][j-k]=0
        switch=0
    if(d1[i][j]>50):
      if(switch==0):
        for k in range(0,3):
            d1[i][j+k]=255
        j=j+4
        switch=1
      else:
        d1[i][j]=0  #do not change if inner part is required

t1=np.uint8(d1)
f1=Image.fromarray(t1)

f1.save('D:\DHARUN\STUDY\SEM 5\Research\Jpg export\dest1p.png')

f1.show()