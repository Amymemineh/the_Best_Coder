n_list = []
n = 0

for _ in range(4):
    train = list(map(int, input().split()))
    n = n - train[0] + train[1] 
    n_list.append(n)
    
n_list.sort()
print(n_list[3])