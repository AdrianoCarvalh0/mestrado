from pyvesto.pipeline import DefaultNetworkBuilder
from pyvesto.image import Image as pvImage
import pyvesto.util as pv_util
import cv2 as cv
import numpy as np
from igraph import *
import matplotlib.pyplot as plt
from PIL import Image
from matplotlib.image import imread
import networkx as nx




path = 'images/3D P0@CTL-3-FC-A_new.tiff'

img = cv.imread(path)


gray_image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)



blurred2 = cv.GaussianBlur(gray_image, (7, 7), 0)
(T, thresh2) = cv.threshold(blurred2, 127, 255, cv.THRESH_BINARY_INV)



#img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_skel = cv.skeletonize(img)




length_threshold = 5


img1 = pvImage(img)
nb = DefaultNetworkBuilder(length_threshold=length_threshold)
graph = nb.apply(img1)