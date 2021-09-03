import cv2
import numpy as np

from igraph import *


if __name__ == '__main__':


    caminho_grafo1 = r'vessel_data/graphs/3D P0@core@numpy@CTL-3-FC-A_new.npy'
    caminho_grafo2 = r'vessel_data/graphs/Development project@Cre ERT2 P14 Peter@core@numpy@S47-P14-AC-B.npy'



    #carregando o grafo
    grafo1 = np.load(caminho_grafo1, allow_pickle=True, encoding='latin1').item()
    grafo2 = np.load(caminho_grafo2, allow_pickle=True, encoding='latin1').item()

    print('Exibindo o grafo 1:')
    #print(grafo1)
    
    #plotando o grafo
    plot(grafo1)

    print('Exibindo o grafo 2:')
    #print(grafo2)
    #linha e profundidade onde estava o nó
    #linha e coluna do vértice
    pos = grafo1.vs["pos_no"]

    #pegar os vizinhos
    #viz = grafo1.

    print(pos[0])
    # plotando o grafo
    plot(grafo2)



