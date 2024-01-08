time = list(map(int, input().split(':')))
h = 0
answer = 0

for t in time:
    if t >= 1 and t <= 12:
        h += 1   
    elif t > 59:
        h += 4

if h < 4:
    answer = h*2 

print(answer)