a, k = map(int, input().split())
cnt = 0


while True:
  if k == a: 
    print(cnt)
    break
  if k % 2 == 0 and k >= a*2:
    k = k / 2
    cnt += 1
  else:
    k = k - 1
    cnt += 1
   