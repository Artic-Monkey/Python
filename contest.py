# (x,y) x//y  x%y


def gcd(x,y):
    a = 0
    r = 0
    run = True

    while run :
            a = x//y
            r = x%y
            if x%y == 0:
                print("gcd is",a)
                run = False
            x = y
            y = r 

for i in range(0,24):
                


#test case
i = 1
n = 3
gcd(n,i)











