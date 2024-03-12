n, m = map(int, input().split())

bundle = []
one = []
result = 0

for _ in range(m):
  a, b = map(int, input().split())
  bundle.append(a)
  one.append(b)

bundle_money = min(bundle)
one_money = min(one)

if bundle_money < one_money*6:
  if bundle_money < one_money * (n%6):
    result = bundle_money * (n//6+1)
  else:
    result = bundle_money * (n//6) + one_money * (n%6)
else:
  result = one_money*n

print(result)




