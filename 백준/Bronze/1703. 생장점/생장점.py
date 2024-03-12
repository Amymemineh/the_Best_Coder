while True:
    n, *tree_list = list((map(int, input().split())))
    sum = 1
    leaf = tree_list[::2]
    cut = tree_list[1::2]
    
    if n == 0:
        break

    for count in range(len(leaf)):
        sum = sum*leaf[count] - cut[count]
    print(sum)