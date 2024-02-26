s = int(input())
cnt = 1
total = 0

while total + cnt <= s:
    total += cnt
    cnt += 1

print(cnt-1)
