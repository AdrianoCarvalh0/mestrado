
import numpy as np
from PIL import Image

from matplotlib.image import imread

def load_image(caminho) :
    img = imread(caminho)
    return img

if __name__ == '__main__':
    path1 = r'vessel_data/images/3D P0@CTL-3-FC-A_new.tiff'
    path2 = r'vessel_data/labels/3D P0@CTL-3-FC-A_new.png'

    print(f'Exibindo a imagem')
    print(load_image(path1))
    print(f'Exibindo o tipo da imagem: {type(load_image(path1))}')


    print(f'Exibindo o label')
    print(load_image(path2))
    print(f'Exibindo o tipo do label: {type(load_image(path2))}')





