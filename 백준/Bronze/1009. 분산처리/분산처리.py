t = int(input())
for _ in range(t):
    a, b = input().split()
    aa = int(a[-1])
    if aa == 1 or aa == 5 or aa == 6:
        print(aa)
    elif aa == 0:
        print(10)
    elif aa == 2 or aa == 3 or aa == 7 or aa == 8:
        b1 = int(b)%4
        if b1 == 0: print((str(aa**4))[-1])
        else: print((str(aa**b1))[-1])
    else: 
        b2 = int(b)%2
        if b2 == 0: print((str(aa**2))[-1])
        else: print(aa)