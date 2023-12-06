tel = int(input())
time = list(map(int, input().split()))

y = 0
m = 0

for t in time:
    y += (10+(t//30)*10)
    m += (15+(t//60)*15)
    
if y>m:
    print("M", m)
elif y<m:
    print("Y", y)
else:
    print("Y", "M", y)