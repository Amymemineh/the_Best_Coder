n, l = map(int, input().split())
a = []
num = 1

while True:
  if str(l) not in str(num):
    a.append(num)
  num += 1
  if len(a) == n: break

print(max(a))