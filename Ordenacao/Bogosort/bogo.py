import timeit
from random import randint, shuffle
import matplotlib.pyplot as plt
from random import *
from time import *

seed()
def geraLista(tam):
    lista = list(range(1, tam + 1))
    shuffle(lista)
    return lista
      

def desenhaGrafico(x,lista1,xl = "Entradas", yl = "Y",name="out", label1 = "Lista 1", label2 = "Lista 2"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x, lista1, label = label1)
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.savefig(name)

def sort(lista):
    bogo(lista)


def inorder(x):
    i = 0
    j = len(x)
    while i + 1 < j:
        if x[i] > x[i + 1]:
            return False
        i += 1
    return True

def bogo(x):
    count = 0    
    while not inorder(x):
        count+=1    
        shuffle(x)
    print(count)	
    return x

quant = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 50, 100]
graf_tempo = []

for i in range(len(quant)):
    print(quant[i])
    lista = geraLista(quant[i])
    graf_tempo.append(timeit.timeit("sort({})".format(lista),setup="from __main__ import sort",number=1))


desenhaGrafico(quant,graf_tempo,"Tamanho", "Tempo", "saida_time", label1 = "Lista")
