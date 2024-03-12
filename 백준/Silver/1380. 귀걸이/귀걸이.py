scenario = 0

while True:
  scenario += 1
  n = int(input())
  name = [input() for i in range(n)]
  number = []
  for _ in range(2*n - 1):
    num, alpha = input().split()
    number.append(int(num))

  for i in range(1, n+1):
    if number.count(i) == 1:
      print(scenario, name[i-1])         
  if n == 0: break
