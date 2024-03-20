l = int(input())
union = list(map(int, input().split()))
n = int(input())
cnt = 0

if n not in union:
  union = sorted(union + [0, n])
  idx = union.index(n)
  before = union[idx - 1]
  after = union[idx + 1]

  for i in range(before + 1, after):
    for j in range(i+1, after):
      if i <= n and j >= n:
        cnt += 1

print(cnt)