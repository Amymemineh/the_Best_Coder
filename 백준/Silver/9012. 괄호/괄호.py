n = int(input())

for _ in range(n):
  text = input()
  stack = []

  for i in text:
    if stack and i == ")" and stack[-1] == "(": stack.pop()
    else: stack.append(i)  
  
  if stack: print("NO")
  else: print("YES")