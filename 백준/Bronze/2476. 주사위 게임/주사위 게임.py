n = int(input())
money_list = []


for _ in range(n):
    a, b, c = sorted(map(int, input().split()))
    if a == b == c:
        money = 10000+1000*a
        money_list.append(money)
    else: 
        if a < b < c:
            money = 100*c
            money_list.append(money)
        else:
            money = 1000+b*100
            money_list.append(money)  

money_list.sort()
print(money_list[-1])