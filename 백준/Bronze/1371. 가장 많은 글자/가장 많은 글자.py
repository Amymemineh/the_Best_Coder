import sys
sens = sys.stdin.read().replace(' ', '').replace('\n', '')
dic = {}

for sen in sens:
  if sen not in dic:
    dic[sen] = 1
  else:
    dic[sen] += 1

answer = [key for key, value in dic.items() if value == max(dic.values())]
print(('').join(sorted(answer)))