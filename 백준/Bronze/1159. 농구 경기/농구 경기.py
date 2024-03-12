n = int(input())
name = []
answer = []

for _ in range(n):
  name.append(input()[0])

first = set(name)

for i in first:
  if name.count(i) >= 5:
    answer.append(i)

if len(answer) > 0:
  print(''.join(sorted(answer)))
else:
  print("PREDAJA")