x, y, w, h = map(int, input().split())
map = min(x, y, w-x, h-y)
print(map)