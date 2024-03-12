song = []
qes = []
time = []
t = 1


n, q = map(int, input().split())

for _ in range(n):
  song.append(int(input()))

for _ in range(q):
  qes.append(int(input()))

for i in song:
  for _ in range(i):
    time.append(t)
  t+=1


for j in qes:
  print(time[j])