# ***Imports***

import cv2
import numpy as np
from igraph import *
import matplotlib.pyplot as plt
from PIL import Image
from matplotlib.image import imread
import networkx as nx


path = r'vessel_data/images/3D P0@CTL-3-FC-A_new.tiff'
img = imread(path)
path = [(20, 40), (20, 41), (20, 42), (21, 43), (22, 44), (23, 44), (24, 44)]

img_viz = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
img_viz[:, :, 0] = img
img_viz[:, :, 1] = img
img_viz[:, :, 2] = img

x, y = zip(*path)
img_viz[x, y, 0] = 255
plt.figure(figsize=[24, 20])
plt.subplot(1, 2, 1)
plt.imshow(img)
plt.subplot(1, 2, 2)
plt.imshow(img_viz)

