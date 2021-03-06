{
 "cells": [],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.6"
  },
  "pycharm": {
   "stem_cell": {
    "cell_type": "raw",
    "source": [
     "# ***Imports***\n",
     "\n",
     "from google.colab.patches import cv2_imshow\n",
     "import cv2\n",
     "import numpy as np\n",
     "from igraph import *\n",
     "import matplotlib.pyplot as plt\n",
     "from PIL import Image\n",
     "from matplotlib.image import imread\n",
     "import networkx as nx\n",
     "\n",
     "\n",
     "# ***Funções***\n",
     "\n",
     "def formando_linhas_colunas(dicionario):\n",
     "   #colando no eixo x e y as posições do grafo\n",
     "   posx = []\n",
     "   posy = []\n",
     "   for key, value in dicionario:\n",
     "      posx.append(value[0])\n",
     "      posy.append(value[1])\n",
     "\n",
     "   return posx, posy\n",
     "\n",
     "\n",
     "def mostrando_esqueleto(pos_eds, img_or):\n",
     "  #construindo uma imagem de zeros para o tamanho da imagem de origem\n",
     "  img = np.zeros((img_or.shape[0], img_or.shape[1]), dtype=np.uint8)\n",
     "  for pos_edge in pos_eds:\n",
     "    for pixel in pos_edge:\n",
     "      img[pixel[1], pixel[2]] =255\n",
     "  return img\n",
     "\n",
     "#MODIFICAR ESTA IMPLEMENTAÇÃO\n",
     "def esqueletando(e1,e2, img_or):\n",
     "  #construindo uma imagem de zeros para o tamanho da imagem de origem\n",
     "  img = np.zeros((img_or.shape[0], img_or.shape[1]), dtype=np.uint8)\n",
     "  for p1 in e1:\n",
     "    for pixel in e2:\n",
     "      img[pixel[1], pixel[2]] =255\n",
     "  return img\n",
     "\n",
     "def transform_img_graph(image_graph):\n",
     "\n",
     "    graphIgraph = np.load(image_graph, allow_pickle=True, encoding='latin1').item()\n",
     "    grafoNx = graphIgraph.to_networkx()\n",
     "\n",
     "    return grafoNx\n",
     "\n",
     "def vertex_position(grafo):\n",
     "  posicao = dict(grafo.nodes(data='pos_no'))\n",
     "  posicao = {node:(posicao[2], img1.shape[0] - posicao[1]) for node,posicao in posicao.items()}\n",
     "  return posicao\n",
     "\n",
     "def plot_graph(grafo):\n",
     "  plt.figure(figsize=[20, 15])\n",
     "\n",
     "  position = vertex_position(grafo)\n",
     "\n",
     "  nx.draw_networkx_nodes(grafo,position, node_size=4)\n",
     "  nx.draw_networkx_edges(grafo,position)\n",
     "\n",
     "  plt.title(\"Grafo\")\n",
     "  #plt.text(0,1,str(grafo.size(weight='weight')), fontdict = None)\n",
     "  plt.plot()\n",
     "\n",
     "\n",
     "#CONTINUAR IMPLEMENTANDO\n",
     "def edges_position(grafo):\n",
     "  ps = grafo.edges\n",
     "  arestas1 = []\n",
     "  arestas2 = []\n",
     "  for p in ps:\n",
     "      arestas1.append(p[1])\n",
     "      arestas2.append(p[2])\n",
     "\n",
     "  return arestas1, arestas2\n",
     "\n",
     "\n",
     "\n",
     "img1 = imread('/content/drive/MyDrive/Mestrado em Ciência da Computação/Testes do Mestrado/vessel_data/images/3D P0@CTL-3-FC-A_new.tiff')\n",
     "img2 = imread('/content/drive/MyDrive/Mestrado em Ciência da Computação/Testes do Mestrado/vessel_data/labels/3D P0@CTL-3-FC-A_new.png')\n",
     "\n",
     "grafo1 = np.load('/content/drive/MyDrive/Mestrado em Ciência da Computação/Testes do Mestrado/vessel_data/graphs/3D P0@core@numpy@CTL-3-FC-A_new.npy', allow_pickle=True, encoding='latin1').item()\n",
     "\n",
     "#Esta função é do igraph. MODIFICÁ-LA\n",
     "pos_edges = grafo1.es[\"pos_ed\"]\n",
     "\n",
     "\n",
     "grafoNX = transform_img_graph('/content/drive/MyDrive/Mestrado em Ciência da Computação/Testes do Mestrado/vessel_data/graphs/3D P0@core@numpy@CTL-3-FC-A_new.npy')\n",
     "\n",
     "#removendo autoloops\n",
     "grafoNX.remove_edges_from(nx.selfloop_edges(grafoNX))\n",
     "\n",
     "#plotando o grafo NX\n",
     "plot_graph(grafoNX)\n",
     "\n",
     "#pega a posição dos vértices no grafo\n",
     "posicao = vertex_position(grafoNX)\n",
     "\n",
     "#pega as posições e coloca no eixo x e y para ser plotado\n",
     "pos1, pos2 = formando_linhas_colunas(posicao.items())\n",
     "\n",
     "\n",
     "#Plotagem das posições do grafo\n",
     "plt.figure(figsize=[24, 10])\n",
     "\n",
     "plt.title(\"Formando linhas e colunas no plot, pegando as posições:\")\n",
     "plt.scatter(pos1, pos2)\n",
     "\n",
     "\n",
     "#formando o esqueleto da imagem com o igraph\n",
     "image = mostrando_esqueleto(pos_edges, img1)\n",
     "\n",
     "plt.figure(figsize=[24, 10])\n",
     "plt.title(\"Imagem esqueletada\")\n",
     "plt.subplot(1, 2, 1)\n",
     "plt.imshow(image, 'gray')\n",
     "plt.title(\"Plot das posições\")\n",
     "plt.subplot(1, 2, 2)\n",
     "plt.scatter(pos1, pos2)\n",
     "\n",
     "\n",
     "\n",
     "\n",
     "# ***Testes com o grafo do networkx***\n",
     "\n",
     "#position = (grafoNX.edges.values())\n",
     "img_cp = img1.copy\n",
     "img_cp = np.zeros((img1.shape[0], img1.shape[1]),  dtype=np.uint8)\n",
     "\n",
     "print(f'Número de arestas: ',grafoNX.number_of_edges())\n",
     "print(f'Número de nós: ', grafoNX.number_of_nodes())\n",
     "\n",
     "print(grafoNX.get_edge_data(7,269))\n",
     "grafo_edge = grafoNX.get_edge_data(7,269)\n",
     "\n",
     "for key, value in grafo_edge.items():\n",
     "  print( value['pos_ed'])\n",
     "\n",
     "\n",
     "pos_x = []\n",
     "pos_y = []\n",
     "\n",
     "\n",
     "for i in range(len(value['pos_ed'])):\n",
     "\n",
     "  pos_x.append(value['pos_ed'][i][1])\n",
     "  pos_y.append(value['pos_ed'][i][2])\n",
     "\n",
     "\n",
     "\n",
     "\n",
     "#imprimindo a imgagem\n",
     "plt.figure(figsize=[12, 6])\n",
     "image_expansive = np.array(img_cp)\n",
     "image_expansive = np.expand_dims(image_expansive, axis=0)  # or axis=1\n",
     "#plt.imshow(image_expansive)\n",
     "plt.show()\n",
     "\n",
     "#imprimindo a imagem em tons de cinza\n",
     "plt.figure(figsize=[12, 6])\n",
     "#plt.plot(image_expansive)\n",
     "#plt.imshow(image_expansive, 'gray')\n",
     "plt.show()\n",
     "\n",
     "#plotando a imagem\n",
     "plt.figure(figsize=[12, 6])\n",
     "plt.plot(img_cp)\n",
     "plt.show()\n",
     "\n",
     "#imprimindo o histograma de forma convencional\n",
     "plt.figure(figsize=[12, 6])\n",
     "plt.hist(img_cp)\n",
     "plt.show()\n",
     "\n",
     "#Plotagem das posições do grafo\n",
     "plt.figure(figsize=[12, 6])\n",
     "plt.title(\"Aresta 7, 269\")\n",
     "plt.scatter(pos_x, pos_y)\n",
     "plt.show()\n",
     "\n",
     "#imprimindo o histograma\n",
     "plt.hist(image_expansive.flatten(), bins=50)\n",
     "plt.xlabel('Intensity')\n",
     "plt.ylabel('Number of pixels')\n",
     "plt.show()\n",
     "\n",
     "grafo_edge = grafoNX.get_edge_data(7,269)\n",
     "#pos_edges = grafo_edge[0]['pos_ed'][0]\n",
     "#print(pos_edges)\n",
     "\n",
     "#path = r\"H:\\datasets\\segmentation\\vessel\\maximum_projection\\images\\3D P0@CTL-3-FC-A_new.tiff\"\n",
     "#img = plt.imread(path)\n",
     "#path = [(20, 40), (20, 41), (20, 42), (21, 43), (22, 44), (23, 44), (24, 44)]\n",
     "\n",
     "img_viz = np.zeros((img1.shape[0], img1.shape[1], 3), dtype=np.uint8)\n",
     "img_viz[:, :, 0] = img1\n",
     "img_viz[:, :, 1] = img1\n",
     "img_viz[:, :, 2] = img1\n",
     "\n",
     "posicaox = []\n",
     "posicaoy = []\n",
     "\n",
     "for i in range(len(grafo_edge[0]['pos_ed'])):\n",
     "  posicaox.append(grafo_edge[0]['pos_ed'][i][1])\n",
     "  posicaoy.append(grafo_edge[0]['pos_ed'][i][2])\n",
     "\n",
     "\n",
     "#x, y = zip(*path)\n",
     "img_viz[posicaox, posicaoy, 0] = 255\n",
     "\n",
     "plt.figure(figsize=[12, 6])\n",
     "\n",
     "plt.imshow(img_viz, 'gray')\n",
     "plt.show()\n",
     "\n",
     "\n",
     "plt.figure()\n",
     "plt.subplot(1, 2, 1)\n",
     "plt.imshow(img_viz)\n",
     "plt.subplot(1, 2, 2)\n",
     "\n",
     "\n",
     "%matplotlib notebook\n",
     "import matplotlib.pyplot as plt\n",
     "import numpy as np\n",
     "\n",
     "path = r\"/content/drive/MyDrive/Mestrado em Ciência da Computação/Testes do Mestrado/vessel_data/images/3D P0@CTL-3-FC-A_new.tiff\"\n",
     "img = plt.imread(path)\n",
     "path = [(20, 40), (20, 41), (20, 42), (21, 43), (22, 44), (23, 44), (24, 44)]\n",
     "\n",
     "img_viz = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)\n",
     "img_viz[:, :, 0] = img\n",
     "img_viz[:, :, 1] = img\n",
     "img_viz[:, :, 2] = img\n",
     "\n",
     "x, y = zip(*path)\n",
     "img_viz[x, y, 0] = 255\n",
     "plt.figure()\n",
     "plt.subplot(1, 2, 1)\n",
     "plt.imshow(img_viz)\n",
     "plt.subplot(1, 2, 2)\n",
     "\n"
    ],
    "metadata": {
     "collapsed": false
    }
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}