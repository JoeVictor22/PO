lis = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
vezes = int(input())
z =1
while (vezes >= z):
    x=input()
    quant=int(input())
    codigo=""
    pos = 1
    for pos in range(len(x)):
        i=0
        while i<26:
            if lis[i] == x[pos]:
                if i-quant < 1:
                    codigo += lis[(i-quant)%26]
                    break
                else:
                    codigo += lis[(i-quant)]
                    break
            i+=1
    z +=1
    print(codigo)
