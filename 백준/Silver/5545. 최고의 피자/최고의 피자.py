n = int(input())
a, b = map(int, input().split())
dough = int(input())
pizza = dough
best = dough / a

if n != 0: 
  topping = sorted([int(input()) for _ in range(n)])

  for i in range(1, n+1):
    pizza += topping[-1]
    if best < pizza / (a + b * i):
      best = pizza / (a + b * i)
      topping.pop()

print(int(best))