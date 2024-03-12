n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a_sort = sorted(a)
b_sort = sorted(b, reverse = True)

result = 0

for i in range(n):
  result += a_sort[i] * b_sort[i]
  
print(result)