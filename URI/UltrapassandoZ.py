x = int(input())
z = int(input())
def ultraZ(x,z):
        while(x >= z):
                z = int(input())
        for i in range(x,z):
                x2 = x
                i = 1
                while x2 < z:
                        x2 = x2 + x + i
                        i=i+1
        print(i)

        
ultraZ(x,z)
