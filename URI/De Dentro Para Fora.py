quant = int(input())
x=1
while (x <= quant):
    frase = input()
    a = int(len(frase))
    b = a//2
    frase2 =""
    b=b-1
    while(b >= 0):
        frase2 = frase2 + frase[b]
        b = b - 1
    b = a//2
    a=a-1
    while(a >= b):
        frase2 = frase2 + frase[a]
        a = a - 1
    print(frase2)
    x=x+1


