def count(lista, maximo):
	count = [0] * maximo
	listaOrdenada = [None] * len(lista)
	for i in range(len(lista)):
		count[lista[i]] += 1
	for i in range(1, maximo):
		count[i] += count[i-1] 
	for i in range(len(lista)):
		listaOrdenada[count[lista[i]]-1] = lista[i]
		count[lista[i]] -= 1
