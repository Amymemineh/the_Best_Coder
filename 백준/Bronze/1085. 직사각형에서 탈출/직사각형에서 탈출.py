x, y, w, h = map(int, input().split())
sq = min(x, y, w-x, h-y)
print(sq)