
import cv2
import numpy as np
from igraph import *
import matplotlib.pyplot as plt
from PIL import Image
from matplotlib.image import imread
import networkx as nx


def formando_linhas_colunas(vertices):
    #colando no eixo x e y as posições do grafo
    posx = []
    posy = []
    for pixel in pos:
        posx.append(pixel[2])
        posy.append(pixel[1])

    return posx, posy

def mostrando_esqueleto(pos_eds, img_or):
    #construindo uma imagem de zeros para o tamanho da imagem de origem
    img = np.zeros((img_or.shape[0], img_or.shape[1]), dtype=np.uint8)
    for pos_edge in pos_eds:
        for pixel in pos_edge:
            img[pixel[1], pixel[2]] =255
    return img



caminho_grafo1 = r'vessel_data/graphs/3D P0@core@numpy@CTL-3-FC-A_new.npy'
caminho_grafo2 = r'vessel_data/graphs/Development project@Cre ERT2 P14 Peter@core@numpy@S47-P14-AC-B.npy'

path1 = r'vessel_data/images/3D P0@CTL-3-FC-A_new.tiff'
path2 = r'vessel_data/labels/3D P0@CTL-3-FC-A_new.png'

img1 = imread(path1)
img2 = imread(path2)


#carregando o grafo
grafo1 = np.load(caminho_grafo1, allow_pickle=True, encoding='latin1').item()
grafo2 = np.load(caminho_grafo2, allow_pickle=True, encoding='latin1').item()



#pegando todas as posições do grafo1, linha e coluna, posição zero(0) não tem informações relavantes
print('Grafo 1:')
pos = grafo1.vs["pos_no"]
pos1, pos2 = formando_linhas_colunas(pos)

print(grafo1.neighbors(0))

pos_edges = grafo1.es["pos_ed"]
image = mostrando_esqueleto(pos_edges, img1)

plt.figure(figsize=[24, 10])
plt.subplot(1, 2, 1)
plt.imshow(image, 'gray')
plt.subplot(1, 2, 2)
plt.scatter(pos1, pos2)


print('Grafo 2:')
pos2 = grafo2.vs["pos_no"]
pos_g2_1, pos_g2_2 = formando_linhas_colunas(pos2)

pos_edges2 = grafo2.es["pos_ed"]
image2 = mostrando_esqueleto(pos_edges2, img2)

plt.figure(figsize=[24, 10])
plt.subplot(1, 2, 1)
plt.imshow(image2, 'gray')
plt.subplot(1, 2, 2)
plt.scatter(pos_g2_1, pos_g2_2)


print("Number of vertices in the graph:", grafo1.vcount())
print("Number of edges in the graph", grafo1.ecount())
print("Is the graph directed:", grafo1.is_directed())
print("Maximum degree in the graph:", grafo1.maxdegree())
print("Quantidade de degrees in the graph:", grafo1.degree())
print("Quantidade de edge_betweenness in the graph:", grafo1.edge_betweenness())
print("Tamanho do grafo: ",len(grafo1.vs.select()))


ebs = grafo1.edge_betweenness()
max_eb = max(ebs)
print("#maior centralidade de intermediação")
print([grafo1.es[idx].tuple for idx, eb in enumerate(ebs) if eb == max_eb])

#print("Adjacency matrix:\n", grafo1.get_adjacency())



print("Vértices com graus maiores que dois")
#print(grafo1.vs.select(_degree_lt=2))

plt.figure(figsize=[30, 20])
grafo_nx = grafo1.to_networkx()
position=nx.random_layout(grafo_nx)
nx.draw_networkx_nodes(grafo_nx,position)
nx.draw_networkx_edges(grafo_nx,position)
#edge_weight=dict([((u,v,),d) for u,v,d in grafo_nx.edges(data=True)])
#edge_weight=dict([((posx,posy,tam)) for posx,posy,tam in grafo_nx.edges(data=True)])
nx.draw(grafo_nx, with_labels=True, font_weight='bold')
#nx.draw_networkx_edge_labels(grafo_nx,position,edge_labels=edge_weight)
#Coloca na imagem o peso total
plt.text(0,1,str(grafo_nx.size(weight='weight')), fontdict = None)
#tamanho do grafo
print(len(grafo_nx))
plt.plot()



layout = grafo1.layout("drl")
plot(grafo1, layout=layout, bbox=(1000,1000))


#mostrar vizinhos do vértice
#for i in range(2270):
#print(grafo1.neighbors (i, mode = ALL))

#print(grafo1.neighbors (1540, mode = ALL))

print(grafo1.es.attribute_names())
print(grafo1.es['is_branch'])
print(grafo1.es['tam'])
#print(grafo1)

#import igraph as ig
visual_style = {}
#out_name = "/content/drive/MyDrive/Mestrado em Ciência da Computação/Testes do Mestrado/graph.png"
# Set bbox and margin
#visual_style["bbox"] = (1000,1000)
visual_style["margin"] = 27
# Set vertex colours
visual_style["vertex_color"] = 'white', 'yellow','green','red','blue'
# Set vertex size
visual_style["vertex_size"] = 10
# Set vertex lable size
visual_style["vertex_label_size"] = 22
# Don't curve the edges
visual_style["edge_curved"] = False
# Set the layout
#my_layout = grafo1.layout_random()
#my_layout = grafo1.layout_reingold_tilford_circular()
my_layout = grafo1.layout_sphere()

visual_style["layout"] = my_layout
# Plot the graph
plot(grafo1,  **visual_style)
#ig.plot(grafo1, target='/content/drive/MyDrive/Mestrado em Ciência da Computação/Testes do Mestrado/myfile.pdf')
#plot(g, "social_network.pdf", **visual_style)



