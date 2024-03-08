n = int(input())
ppl = sorted(list(int(input()) for _ in range(n)), reverse = True)
tip_list = []

for i in range(n):
  tip = ppl[i] - i
  if tip < 0: tip = 0
  tip_list.append(tip)

print(sum(tip_list))
