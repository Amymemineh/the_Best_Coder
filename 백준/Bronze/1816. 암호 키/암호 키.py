n = int(input())
num = [int(input()) for i in range (n)]
for su in num:
  for i in range(10**6, 1, -1):
    if su%i == 0:
      print("NO")
      break
  else: print("YES")