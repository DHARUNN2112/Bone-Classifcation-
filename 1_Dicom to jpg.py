import pydicom as pd
import numpy as np
from PIL import Image

d=pd.dcmread('D:\DHARUN\STUDY\SEM 5\Research\Dicom Sample\D22760')     #reading the dicom image

n=d.pixel_array.astype(float)                                                   #extracting pixel array                
s=(np.maximum(n,0)/n.max())*255                                                 #changing the scale [0-255]
s1=np.uint8(s)                                                                  #changing to 8 bit unsigned integer        
f=Image.fromarray(s1)                                                           #Creating the Image from the array

f.save('D:\DHARUN\STUDY\SEM 5\Research\Jpg export\est1.jpg')                  #Saving it as the JPG file 
f.save('D:\DHARUN\STUDY\SEM 5\Research\Jpg export\est1p.png')
#f.show()
