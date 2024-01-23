a, b = map(int, input().split())
num = []

for i in range(1, b+1):
  for _ in range(i):
    num.append(i)
    if len(num) >= b: break

answer = sum(num[a-1:b])
print(answer)