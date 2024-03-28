n,m=map(int,input().split())
dic={}

for _ in range(n):
  team = input()
  num = int(input())
  member = sorted([input() for _ in range(num)])
  dic[team] = member

for _ in range(m):
  quiz = input()
  kind = int(input())
  if kind == 0:
    for i in dic[quiz]:
      print(i)
  else:
    for key in dic.keys():
      if quiz in dic[key]:
        print(key)