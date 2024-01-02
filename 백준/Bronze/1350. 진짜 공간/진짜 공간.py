n = int(input())
files = list(map(int,input().split()))
c = int(input())


cnt = 0

for file in files:
  if file > 0:
    cnt += (file-1)//c + 1
  else:
    pass

print(c*cnt)
