e, s, m = map(int, input().split())
a, b, c = 1, 1, 1
cnt = 1

while True:
  if e == a and s == b and m == c: break
  a += 1
  b += 1
  c += 1
  if a > 15: a = 1
  if b > 28: b = 1
  if c > 19: c = 1
  cnt += 1

print(cnt)