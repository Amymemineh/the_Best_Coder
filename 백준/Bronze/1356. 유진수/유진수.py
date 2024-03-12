n = input()

for i in range(1, len(n)):
  a = n[:i]
  b = n[i:]
  
  mul_a = mul_b = 1
  
  for aa in a:
    mul_a *= int(aa)

  for bb in b:
    mul_b *= int(bb)

  if mul_a == mul_b:
    print("YES")
    break
  
else: print("NO")