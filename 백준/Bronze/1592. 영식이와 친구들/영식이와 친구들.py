N, M, L = map(int, input().split())
cnt = 0
start = 0
seat = [0] * N
seat[0] = 1

while seat[start] < M:   
  if seat[start]%2 != 0:
    start = (start + L) % N
  else:
    start = (start - L) % N
  seat[start] += 1
  cnt += 1

print(cnt)