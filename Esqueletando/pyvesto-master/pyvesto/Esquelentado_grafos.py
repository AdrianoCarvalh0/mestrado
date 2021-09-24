from pipeline import DefaultNetworkBuilder
from image import Image as pvImage
import util as pv_util
import cv2
import numpy as np
from igraph import *
import matplotlib.pyplot as plt
from PIL import Image
from matplotlib.image import imread
import networkx as nx

length_threshold = 5

img1 = imread('/content/drive/MyDrive/Mestrado em Ciência da Computação/Testes do Mestrado/vessel_data/images/3D P0@CTL-3-FC-A_new.tiff')
img = pvImage(img1)
nb = DefaultNetworkBuilder(length_threshold=length_threshold)
graph = nb.apply(img)