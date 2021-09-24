import cv2
import numpy as np
import matplotlib.pyplot as plt
from igraph import *

def plotando(grafo):
    posx = []
    posy = []
    for pixel in pos:
        posx.append(pixel[2])
        posy.append(pixel[1])

    plt.scatter(posx, posy)


if __name__ == '__main__':


    caminho_grafo1 = r'vessel_data/graphs/3D P0@core@numpy@CTL-3-FC-A_new.npy'
    caminho_grafo2 = r'vessel_data/graphs/Development project@Cre ERT2 P14 Peter@core@numpy@S47-P14-AC-B.npy'
    #carregando o grafo
    grafo1 = np.load(caminho_grafo1, allow_pickle=True, encoding='latin1').item()
    grafo2 = np.load(caminho_grafo2, allow_pickle=True, encoding='latin1').item()

    print('Plotando o grafo 1:')
    pos = grafo1.vs["pos_no"]
    plotando(pos)
    #print(grafo1)
    #pegando todas as posições do grafo1, linha e coluna, posição zero(0) não tem informações relavantes

    #colando no eixo x as posições do grafo


    #print("Adjacency matrix:\n", grafo1.get_adjacency())

    #plotando o grafo
    #plot(grafo1)


    #pegar os vizinhos
    #viz = grafo1.

    print(pos[0])

    #atributos do grafo
    print(grafo1.es.attribute_names())
    #mostrando todos as posições da posição zero
    print(grafo1.es[0]['pos_ed'])



