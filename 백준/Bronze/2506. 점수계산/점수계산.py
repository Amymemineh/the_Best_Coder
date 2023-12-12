n = int(input())
plus = list(map(int, input().split()))

sum = 0
result = 0

for i in plus:
    if i == 1:
        sum+=1
        result += sum

    else: 
        sum = 0

print(result)