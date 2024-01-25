t = int(input())

for i in range(t):
  input()
  n, m = map(int, input().split())
  jun = sorted([int(j) for j in input().split()])
  bi = sorted([int(b) for b in input().split()])
  
  while jun and bi:
    if jun[0] < bi[0]:
      jun.pop(0)
    else:
      bi.pop(0)
  
  if jun: print("S")
  elif bi: print("B")
  else: print("C")