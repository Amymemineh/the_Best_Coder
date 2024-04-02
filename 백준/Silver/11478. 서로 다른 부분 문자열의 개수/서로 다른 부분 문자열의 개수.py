s = input()
answer = set()
n = 0

while n <= len(s):
  for i in range(len(s) - n):
    answer.add(s[i:i+(n+1)])
  n += 1
  
print(len(answer))