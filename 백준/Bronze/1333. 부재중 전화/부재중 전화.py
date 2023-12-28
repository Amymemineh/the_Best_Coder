n, l, d = map(int, input().split())

time = (n*l) + 5*(n-1)
rest = []
answer = d

for i in range(l, time, l+5):
  for j in range(5):
    rest.append(i+j)
    l += 5

while True:
  if answer < time:
    if answer in rest:
      print(answer)
      break
    else:
      answer += d
  else:
    print(answer)
    break