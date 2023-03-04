import numpy as np
from random import randint
from math import * 
class Kmeans:
    def __init__(self, clust):
        self.k = clust
        self.centroide = list()
        self.clusters = list()

    def distancia(self, x, y):
        for i in range(0, len(x)):
            for j in range(0, self.k):
                menor = 9999999999.0
                posi = 0.0
                cont =0.0
                for k in range(0, len(self.centroide[0])):
                    hipotenusa = pow((x[i] - self.centroide[k][0]), 2) + pow((y[i] - self.centroide[k][1]), 2)
                    hipotenuza = sqrt(hipotenusa)
                    if hipotenusa < menor:
                        menor = hipotenusa
                        posi = cont
                    posi += 1
                temp = [x[i], y[i]]
                self.clusters[posi].append(temp)

    def analize(self, x, y):
        def distancia(x, y):
            for i in range(0, len(x)):
                for j in range(0, self.k):
                    menor = 9999999999
                    posi = 0
                    cont =0
                    for k in range(0, len(self.centroide[0])):
                        hipotenusa = pow((x[i] - self.centroide[k][0]), 2) + pow((y[i] - self.centroide[k][1]), 2)
                        hipotenuza = sqrt(hipotenusa)
                        if hipotenusa < menor:
                            menor = hipotenusa
                            posi = cont
                        posi += 1
                    temp = [x[i], y[i]]
                    self.clusters[posi].append(temp)
        quant = len(x)
        array = list()
        while (len(array) < self.k):
            posi = randint(0, quant-1)
            if posi not in array:
                array.append(posi)
        for i in range(0, self.k):
            temp = [x[array[i]], y[array[i]]]
            self.centroide.append(temp)
        for i in range(0, self.k):
            temp = []
            self.clusters.append(temp)
        print(self.centroide)
        distancia(x, y)
        print(self.clusters)
        print(self.centroide)
        


kmeans = Kmeans(3)
x = [2, 2, 8, 5, 7, 6, 1, 4]
y = [10, 5, 4, 8, 5, 4, 2, 9]
kmeans.analize(x, y)
