from typing import Dict
a, b, c = map(int, input().split())
sum = []
dict = {}

for aa in range(1, a+1):
  for bb in range(1, b+1):
    for cc in range(1, c+1):
       sum.append(aa + bb + cc)

for i in sum:
  if i not in dict:
    dict[i] = 1
  else:
    dict[i] += 1

answer = max(dict, key = dict.get)

print(answer)