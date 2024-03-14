n = int(input())
x = n // 5

for i in range(x, -1, -1):
  y = n - (5 * i)
  mock, nam = divmod(y, 3)
  if nam == 0:
    print(i + mock)
    break
else: print(-1)