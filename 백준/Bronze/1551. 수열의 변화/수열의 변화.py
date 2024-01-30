n, k = map(int, input().split())
num = list(map(int,input().split(",")))
repeat = 0
new = num.copy()

while repeat < k:
  number = []
  for i in range(1, len(new)):
    number.append(new[i] - new[i-1])
  repeat += 1
  new = number.copy()

print(",".join(map(str, new)))