
def insertion(lista):
  for x in range(0, len(lista)):
    key = lista[x]
    y = x-1
    while key < lista[y] and y>=0:
      lista[y+1] = lista[y]
      y-=1
    lista[y+1] = key
