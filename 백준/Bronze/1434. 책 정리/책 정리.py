n, m = map(int, input().split())

box = list(map(int, input().split()))
book = list(map(int, input().split()))

cnt = 0

for i in range(m):
  if book[i] <= box[cnt]:
    box[cnt] -= book[i]
  else:
    while book[i] > box[cnt]:
      cnt += 1
    box[cnt] -= book[i]      

print(sum(box))
  