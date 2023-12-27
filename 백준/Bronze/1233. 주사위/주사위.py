
a, b, c = map(int, input().split())
sum = []
dic = {}

for aa in range(1, a+1):
  for bb in range(1, b+1):
    for cc in range(1, c+1):
       sum.append(aa + bb + cc)

for i in sum:
  if i not in dic:
    dic[i] = 1
  else:
    dic[i] += 1

answer = max(dic, key = dic.get)

print(answer)