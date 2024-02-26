n, m = map(int, input().split())

if n == 0: print(0)
else: 
  cnt = 1
  box = m
  book = list(map(int, input().split()))
  for i in book:
    if box < i:
      box = m  
      cnt += 1
    box -= i  
  print(cnt)