n, l = map(int, input().split())
water = sorted(list(map(int, input().split())))
tape = 1
i = 0
cnt = 1

while True:
  if i + cnt >= n: break
  length = water[i] - 0.5 + l 
  if water[i+cnt] <= length:
    cnt += 1
  else:
    tape += 1
    i += cnt
    cnt = 1

print(tape)