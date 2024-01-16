n = int(input())
num = list(map(int, input().split()))

first = min(num)
last = max(num)

print(first * last)