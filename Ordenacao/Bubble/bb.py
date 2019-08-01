import timeit
from random import randint
import matplotlib.pyplot as plt
from multiprocessing import process

def geraLista(tam):
    lista = []
    while tam:
        lista.append(tam)
        tam-=1
    return lista

def desenhaGrafico(x,lista,xl = "Entradas", yl = "Y",nam="out"):
   # fig = plt.figure(figsize=(10, 13))
   # ax = fig.add_subplot(111)
    plt.plot(x,lista, label = "Bubble Sort")
    plt.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.savefig(nam)

graf_operacoes =[]
def bb(lista):
    count = 0
    for i in range(len(lista)):
        for k in range(i, len(lista)):
            count+=1
            if lista[i] > lista[k]:
                lista[i], lista[k] = lista[k], lista[i]
    graf_operacoes.append(count)

quant = [10000, 20000, 50000, 100000]
graf_tempo = []

for i in range(len(quant)):
    print(quant[i])
    lista = geraLista(quant[i])
    graf_tempo.append(timeit.timeit("bb({})".format(lista),setup="from __main__ import bb",number=1))

desenhaGrafico(quant,graf_tempo,"Tamanho", "Tempo", "saida_time")
desenhaGrafico(quant,graf_operacoes , "Tamanho", "Operações", "saida_operacoes")
