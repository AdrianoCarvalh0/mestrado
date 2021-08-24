import cv2
import numpy as np

from igraph import *
from matplotlib import pyplot as plt

from PIL import Image

path = r'vessel_data/images/3D P0@CTL-3-FC-A_new.tiff'
image = Image.open(path)

im = cv2.imread(path,0)
print(im.dtype)

image.show()
# path
path = r'vessel_data/images/3D P0@CTL-3-FC-A_new.tiff'

# Using cv2.imread() method
img = cv2.imread(path,-1)

# Displaying the image
cv2.imshow('image', img)



#data = np.load('vessel_data/graphs/3D P0@core@numpy@CTL-3-FC-A_new.npy', allow_pickle=True, encoding='latin1').item()


#print(data)
#plot(data)




