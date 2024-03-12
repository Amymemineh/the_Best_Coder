n, m = map(int, input().split())
castle = [input() for _ in range(n)]

sero = [0] * n
garo = [0] * m

sero_cnt = garo_cnt = 0

for i in range(n):
  for j in range(m):
    if castle[i][j] == 'X':
      sero[i] = 1
      garo[j] = 1

sero_cnt = sero.count(0)
garo_cnt = garo.count(0)

print(max(sero_cnt, garo_cnt))