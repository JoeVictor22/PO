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
    bucket(lista)

def bucket(lista):
    tamanho = max(lista)/len(lista)
    bucket = [[] for _ in range(len(lista))]

    for i in range(len(lista)):
        j = int(lista[i] / tamanho)
        if j != len(lista):
            bucket[j].append(lista[i])
        else:
            bucket[len(lista) - 1].append(lista[i])

    for i in range(len(lista)):
        merge(bucket[i])
    lista_ordenada = []
    for i in range(len(lista)):
        lista_ordenada = lista_ordenada + bucket[i]

  


def merge(lista): 
    if len(lista) >1: 
        meio = int(len(lista)/2)
        esquerda = [] 
        direita = []
        for i in range(0, meio):
            esquerda.append(lista[i])
        for i in range(meio, len(lista)):
            direita.append(lista[i])
  
        merge(esquerda) 
        merge(direita) 
  
        i = j = k = 0     
        while i < len(esquerda) and j < len(direita): 
            if esquerda[i] < direita[j]: 
                lista[k] = esquerda[i] 
                i+=1
            else: 
                lista[k] = direita[j] 
                j+=1
            k+=1
          
        while i < len(esquerda): 
            lista[k] = esquerda[i] 
            i+=1
            k+=1
          
        while j < len(direita): 
            lista[k] = direita[j] 
            j+=1
            k+=1

quant = [100000,200000,400000,500000,1000000,2000000]
graf_tempo = []

for i in range(len(quant)):
    print(quant[i])
    lista = geraLista(quant[i])
    graf_tempo.append(timeit.timeit("sort({})".format(lista, quant[i]),setup="from __main__ import sort",number=1))


desenhaGrafico(quant,graf_tempo,"Tamanho", "Tempo", "saida_time", label1 = "Lista")
