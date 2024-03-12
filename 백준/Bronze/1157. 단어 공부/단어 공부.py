word = input().upper()
al = {}

for w in word:
  if w in al:
    al[w] += 1
  else:
    al[w] = 1

answer = [k for k, v in al.items() if max(al.values()) == v]
if len(answer) > 1:
  print("?")
else:
  print(answer[0])