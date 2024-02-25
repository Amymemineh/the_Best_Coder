import math

n = math.factorial(int(input()))
n_rev = str(n)[::-1]
cnt = 0

for i in n_rev:
  if i == '0':
    cnt += 1
  else:
    break

print(cnt)