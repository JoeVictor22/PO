
import timeit
from random import randint
import matplotlib.pyplot as plt

def geraListaInvertida(tam):
    lista = []
    while tam:
        lista.append(tam)
        tam-=1
    return lista

      
def geraLista(tam):
    lista = []
    for i in range(tam):
        n = randint(1,1*tam)
        if n not in lista: lista.append(n)
    return lista

def desenhaGrafico(x,lista1,xl = "Entradas", yl = "Y",name="out", label1 = "Lista 1", label2 = "Lista 2"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x, lista1, label = label1)
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.savefig(name)

def sort(lista, inicio = 0, fim = 0):
	i = inicio
	f = fim-1
	pivo = lista[int((inicio+fim)/2)]
	while(i <= f):
		while(lista[i] < pivo and i < fim):
			i= i + 1
		while(lista[f] > pivo and f > inicio):
			f= f -1
		if i <= f:
			lista[i], lista[f] = lista[f],lista[i]
			i = i + 1
			f = f - 1
	if f > inicio:
		sort(lista, inicio, f+1)
	if i < fim:
		sort(lista, i, fim)


quant = [100000,200000,400000,500000,1000000,2000000]
#quant = list(range(1, 1000, +1))
graf_tempoInvertida = []

#quant = list(range(1, 1000, +1))

print("Lista Invertida")
for i in range(len(quant)):
    print(quant[i])
    listaInvertida = list(range(quant[i], 0, -1))
    graf_tempoInvertida.append(timeit.timeit("sort({},{},{})".format(listaInvertida, 0, len(listaInvertida)),setup="from __main__ import sort",number=1))


desenhaGrafico(quant,graf_tempoInvertida,"Tamanho", "Tempo", "saida_time", label1 = "Lista Invertida")

