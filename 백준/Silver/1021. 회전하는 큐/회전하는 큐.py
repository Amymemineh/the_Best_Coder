from collections import deque

n, m = map(int, input().split())
num = deque(range(1, n+1))
spot = list(map(int, input().split()))
cnt = 0

for i in spot:
  idx = num.index(i)
  cnt += min(idx, len(num)-idx)
  num.rotate(-idx)
  num.popleft()
  
print(cnt)