n,m=map(int, input().split())
j=set(map(int, input().split()))
p=0
k=0
for i in range(1,n+1):
    if i not in j:
        k+=7 if not p else min(7, (i - p)*2)
        p=i
print(k)