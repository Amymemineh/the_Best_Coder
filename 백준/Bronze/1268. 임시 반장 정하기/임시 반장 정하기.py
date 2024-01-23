n = int(input())
ban = []
student =[[0]*n for _ in range(n)]

for i in range(n):
  ban.append(list(map(int, input().split())))

for i in range(5):
  for j in range(n):
    for k in range(j+1, n):
      if ban[j][i] == ban[k][i]:
        student[j][k] = 1
        student[k][j] = 1

cnt = []
cnt = [s.count(1) for s in student]

print(cnt.index(max(cnt))+1)