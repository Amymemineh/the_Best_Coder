import math
d, h, w = map(int, input().split())
t = d/math.sqrt(h**2 + w**2)
print(math.floor(h*t), math.floor(w*t))