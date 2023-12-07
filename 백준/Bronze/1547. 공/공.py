m = int(input())
line = [1, 2, 3]

for i in range(m):
    x, y = map(int, input().split())
    a = line.index(x)
    b = line.index(y)
    line[a], line[b] = line[b], line[a]
if line[0]:
    print(line[0])
else:
    print("-1")