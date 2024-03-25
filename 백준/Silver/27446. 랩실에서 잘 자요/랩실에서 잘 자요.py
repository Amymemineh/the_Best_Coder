n, m = map(int, input().split())
journal = set(map(int, input().split()))
page = 0
ink = 0
for i in range(1, n + 1):
    if i not in journal:
        ink += 7 if not page else min(7, (i - page) * 2)
        page = i
print(ink)