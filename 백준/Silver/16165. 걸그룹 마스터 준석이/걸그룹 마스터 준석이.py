n,m = map(int,input().split())
dic = {}

for _ in range(n):
  team = input()
  member = sorted([input() for _ in range(int(input()))])
  dic[team] = member

for _ in range(m):
  quiz = input()
  kind = int(input())
  if kind == 0:
    print(*dic[quiz], sep = '\n')
  else:
    for key, value in dic.items():
      if quiz in value:
        print(key)