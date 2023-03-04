from math import *
def distanciaEuclidiana(ponto, centroide):
    quant = len(ponto)
    distancia = 0
    for i in range(0, quant):
        distancia += pow((ponto[i] - centroide[i]), 2)
    distancia = sqrt(distancia)
    return distancia

def mostClose(x, y):
    array = [[], []]
    for i in x:
        dis = 9999999
        cont =0
        posi = 0
        for j in y:
            if (distanciaEuclidiana(i, j) < dis):
                dis = distanciaEuclidiana(i, j)
                posi = cont
            cont += 1
        array[posi].append(i)
    print(array)


x = [[1, 4], [2, 6], [1, 9], [2, 8], [3, 4]]
y = [[3, 2], [4, 6]]
for i in range(0, 5):
    print(distanciaEuclidiana(x[i], y[0]))
print("#########################")
for i in range(0, 5):
    print(distanciaEuclidiana(x[i], y[1]))
print("#########################")
mostClose(x, y)
#distanciaEuclidiana(x, y)






























"""from sklearn.cluster import KMeans
import numpy as np

# Cria um array com os pontos de dados
X = np.array([[1, 2, 3], [1, 4, 5], [1, 0, 0], [4, 2, 1], [4, 4, 6], [4, 0, 4]])

# Cria um objeto KMeans com dois clusters
kmeans = KMeans(n_clusters=2)

# Aplica o algoritmo KMeans ao conjunto de dados
kmeans.fit(X)

# Obtém os centróides dos clusters
centroids = kmeans.cluster_centers_

# Obtém as etiquetas de cluster para cada ponto de dados
labels = kmeans.labels_

# Imprime os centróides e as etiquetas
print("Centroids:\n", centroids)
print("Labels:\n", labels)"""