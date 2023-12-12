n, k = map(int, input().split())
i_list = sorted([])

for i in range(1, n+1):
    if n%i == 0:
        i_list.append(i)

if len(i_list) < k:
    print(0)

else: 
    print(i_list[k-1])