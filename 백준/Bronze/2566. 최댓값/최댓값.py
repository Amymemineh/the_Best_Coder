num_list = []
max_num = 0
h = 0
y = 0

for _ in range(9):
    num_list.append(list(map(int,input().split())))

for i in range(9):
    for j in range(9):
        if num_list[i][j] >= max_num:
            max_num = num_list[i][j]
            h = i+1
            y = j+1

print(max_num)
print(h, y)