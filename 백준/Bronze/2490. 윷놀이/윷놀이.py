for _ in range(3):
    yut_list = list(map(int, input().split()))
    if sum(yut_list) == 0:
        print ("D")
    elif sum(yut_list) == 1:
        print ("C")
    elif sum(yut_list) == 2:
        print ("B")
    elif sum(yut_list) == 3:
        print ("A")
    else: print("E")    