n = int(input())
garo = [list(input()) for _ in range(n)]
sero = list(zip(*garo))

def noop(x):
  cnt = 0
  for i in x:
    for j in ''.join(i).split('X'):
      if len(j) >= 2:
        cnt += 1
  return cnt

print(noop(garo), noop(sero))