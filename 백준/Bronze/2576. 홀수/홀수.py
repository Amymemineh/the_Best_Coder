num = []
hol = []

for _ in range(7):
    num.append(int(input()))

for i in num:
    if i%2 == 1:
        hol.append(i)

if len(hol) > 0:
    print(sum(hol))
    print(min(hol))        

else:
    print(-1)