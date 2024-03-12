n = int(input())
dasom, *hubo = [int(input()) for _ in range(n)]
pyo = 0

if not hubo:
  print(pyo)
else:
  while dasom <= max(hubo):
    hubo[hubo.index(max(hubo))] -= 1
    dasom += 1
    pyo += 1
  print(pyo)