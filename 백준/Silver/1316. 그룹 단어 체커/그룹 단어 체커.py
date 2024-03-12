n = int(input())
voca = [input() for _ in range(n)]
no = 0

for v in voca:
  for i in range(len(v)-1):
    if v[i] == v[i+1]: pass
    else:
      if v[i] in set(v[i+1:]):
        no += 1
        break

print(n - no)