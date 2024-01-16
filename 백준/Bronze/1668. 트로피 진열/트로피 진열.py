N = int(input())
trophy = [int(input()) for i in range(N)]
cnt = trophy[0]

left = 1

for t in trophy:
  if t > cnt:
    left += 1
    cnt = t

trophy.reverse()
tnc = trophy[0]

right = 1

for y in trophy:
  if y > tnc:
    right += 1
    tnc = y
 
print(left, right, sep = '\n')