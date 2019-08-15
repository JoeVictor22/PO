def sort(lista): 
    if len(lista) >1: 
        meio = int(len(lista)/2)
        esquerda = [] 
        direita = []
        for i in range(0, meio):
            esquerda.append(lista[i])
        for i in range(meio, len(lista)):
            direita.append(lista[i])
  
        mergeSort(esquerda) 
        mergeSort(direita) 
  
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
