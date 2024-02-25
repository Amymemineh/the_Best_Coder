x = input()
cnt = 0

while len(x) > 1:
    x = str(sum(map(int, x)))
    cnt += 1

print(cnt)
print("YES" if int(x) % 3 == 0 else "NO")