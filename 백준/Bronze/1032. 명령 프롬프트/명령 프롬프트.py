n = int(input())
first, *other = [input() for i in range(n)]

for i in other:
  for j in range(len(i)):
    if first[j] != i[j]:
      first = first[:j] + '?' + first[j+1:]

print(first)