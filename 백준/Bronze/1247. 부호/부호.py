import sys
input=sys.stdin.readline
answer=[]
for i in range(3):
    n=int(input())
    sum = 0
    for a in range(n):
        sum+=int(input())
    if sum==0:
        answer.append("0")
    elif sum>0:
        answer.append("+")
    else:
        answer.append("-")
for items in answer:
    print(items)