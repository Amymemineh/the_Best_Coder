import random

x = int(input())
stick = [64, 32, 16, 8, 4, 2, 1]
hubo = set()

if x in stick: print(1)
else:
  while sum(hubo) != x:
    hubo.add(random.choice(stick))
    if sum(hubo) > x: 
      hubo = set()
  print(len(hubo))