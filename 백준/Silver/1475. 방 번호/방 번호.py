n = input().replace('9', '6')
num = [1, 1, 1, 1, 1, 1, 2, 1, 1]
use = [1, 1, 1, 1, 1, 1, 2, 1, 1]
cnt = 1

for i in n:
  use[int(i)] -= 1
  if use[int(i)] < 0:
    use = [num[j] + use[j] for j in range(len(num))]
    cnt += 1

print(cnt)
