a, b = map(int, input().split())
max = (b//2)+1
num = []

for i in range(1, max+1):
  for _ in range(i):
    num.append(i)

answer = sum(num[a-1:b])
print(answer)