number = sorted(list(map(int, input().split())))
n_max = number[0]*number[1]*number[2]

for i in range(number[2], n_max+1):
  cnt = 0
  for n in number:
    if i%n == 0:
      cnt += 1
    if cnt == 3:
      print(i)
      break
  if cnt == 3:
    break