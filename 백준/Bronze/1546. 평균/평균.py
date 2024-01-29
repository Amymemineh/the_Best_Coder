n = int(input())
num = list(map(int, input().split()))
max_value = max(num) 
print(sum([(new / max_value) * 100 for new in num]) / n)