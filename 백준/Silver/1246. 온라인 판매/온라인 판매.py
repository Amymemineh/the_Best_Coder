n, m = map(int, input().split())
customer = sorted([int(input()) for _ in range(m)])

price = 0
result = 0

for i in range(len(customer)):
    sum_price = customer[i] * min(n, len(customer) - i)
    if sum_price > result:
        price = customer[i]
        result = sum_price

print(price, result)