n, m = map(int, input().split())
cnt = 1
box = m

if n != 0: 
  book = list(map(int, input().split()))
  for i in book:
    if box < i:
      box = m  
      cnt += 1
    box -= i  
  print(cnt)

else: print(0)