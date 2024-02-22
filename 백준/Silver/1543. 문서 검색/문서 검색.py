words = input()
voca = input()
cnt = 0

while voca in words:
  cnt += 1
  idx = words.find(voca)
  words = words[idx+len(voca):]

print(cnt)