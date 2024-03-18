n = int(input())
score = [int(input()) for _ in range(n)]
cnt = 0

for i in range(n-2, -1, -1):
  if score[i] < score[i+1]: pass
  else:
    while score[i] >= score[i+1]:
      score[i] -= 1
      cnt += 1

print(cnt)