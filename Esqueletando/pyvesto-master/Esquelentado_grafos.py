from pyvesto.pipeline import DefaultNetworkBuilder
from pyvesto.image import Image as pvImage
import pyvesto.util as pv_util
import cv2
import numpy as np
from igraph import *
import matplotlib.pyplot as plt
from PIL import Image
from matplotlib.image import imread
import networkx as nx

#from pyvesto.skeleton import skeletonize

length_threshold = 5

img1 = imread('vessel_data/images/3D P0@CTL-3-FC-A_new.tiff')

#teste = skeletonize(img1)
#print(teste)

img = pvImage(img1)
nb = DefaultNetworkBuilder(length_threshold=length_threshold)
graph = nb.apply(img)