n, m = map(int, input().split())
image = [[0]*100 for _ in range(100)]
cnt = 0

for _ in range(n):
    lx, ly, rx, ry = map(int, input().split())
    for i in range(lx-1, rx):
        for j in range(ly-1, ry):
            image[i][j] += 1

for i in range(100):
  for j in range(100):
    if image[i][j] > m:
      cnt += 1

print(cnt)
