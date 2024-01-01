cnt = 1
result = []

while True:
  o, w = map(int, input().split())
  if o == 0:
    break

  while True:
    act, n = input().split()
    if act == 'F' and w > 0:
      w += int(n)
    elif act == 'E' and w > 0:
      w -= int(n)
    elif act == '#':
        result.append((cnt, w, o))
        cnt += 1
        break

for i in result:
  if i[1] > 0.5*i[2] and i[1] < 2*i[2]:
    print(i[0], ':-)')
  elif i[1] <= 0:
    print(i[0], 'RIP')
  else:
    print(i[0], ':-(')