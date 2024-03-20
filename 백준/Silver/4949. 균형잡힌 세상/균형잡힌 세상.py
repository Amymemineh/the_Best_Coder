while True:
  text = input()
  if text == ".": break

  stack = []
  
  for i in text:
    if i == "(" or i == "[": stack.append(i) 
    elif i == ")":
      if len(stack) != 0 and stack[-1] == "(": stack.pop()
      else: 
        stack.append(i)
        break
    elif i == "]":
      if len(stack) != 0 and stack[-1] == "[": stack.pop()
      else: 
        stack.append(i)
        break
        
  if stack: print("no")
  else: print("yes")