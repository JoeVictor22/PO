import timeit
from random import randint, shuffle
import matplotlib.pyplot as plt

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
    shell(lista)

def shell(lista):
    count=0
    gap = int(len(lista)/2)
    
    while (gap > 0):
    
        for i in range(gap,len(lista)):
        
            aux = lista[i]
            j = i
            while(lista[j-gap] > aux and j >= gap  ):
                lista[j] = lista[j-gap]
                j = j-gap
                count+=1
            lista[j] = aux
            count+=1
            
        gap = int(gap/2)

quant = [100000,200000,400000,500000,1000000,2000000]
graf_tempo = []

for i in range(len(quant)):
    print(quant[i])
    lista = geraLista(quant[i])
    graf_tempo.append(timeit.timeit("sort({})".format(lista),setup="from __main__ import sort",number=1))


desenhaGrafico(quant,graf_tempo,"Tamanho", "Tempo", "saida_time", label1 = "Lista")
