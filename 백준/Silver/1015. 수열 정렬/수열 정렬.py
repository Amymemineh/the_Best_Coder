n = int(input())
a = list(map(int, input().split()))
a_sort = sorted(a)

p_list = []

for i in range(n):
  idx = a_sort.index(a[i])
  p_list.append(idx)
  a_sort[idx] = -1

print(*p_list)