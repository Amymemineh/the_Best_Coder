n = input()

if len(n) == 1:
  n = '0' + n

a = n
cnt = 0

while True:
  sum = str(int(a[0]) + int(a[-1]))
  a = a[-1] + sum[-1]
  cnt += 1
  if a == n: break

print(cnt)
