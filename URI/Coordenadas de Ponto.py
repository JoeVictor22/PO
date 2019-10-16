"Coordenadas de um Ponto"
c = input()
num = c.split(" ")
a = float(num[0])
b = float(num[1])

if a > 0.0 and b > 0.0:
    print("Q1")
else:
    if a < 0.0 and b > 0.0:
        print("Q2")
    else:
        if a < 0.0 and b < 0.0:
            print("Q3")
        else:
            if a > 0.0 and b < 0.0:
                print("Q4")
            else:
                if a == 0.0 and b != 0.0:
                    print("Eixo Y")
                else:
                    if a != 0.0 and b == 0.0:
                        print("Eixo X")
                    else:
                        if a == 0.0 and b == 0.0:
                            print("Origem")

        
