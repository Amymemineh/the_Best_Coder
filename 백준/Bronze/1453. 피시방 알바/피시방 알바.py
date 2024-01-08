n = int(input())
seat = list(map(int, input().split()))
unique = set()
cnt = 0


for s in seat:
  if s in unique:
    cnt += 1
  else:
    unique.add(s)

print(cnt)