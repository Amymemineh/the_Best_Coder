n, m = map(int, input().split())
journal = set(map(int, input().split()))
paper = []

for i in range(1, n+1):
  if i not in journal:
    paper.append(i)

page = 0
ink = 0

for i in paper:
  if page:
    ink += min(7, (i - page) * 2)
  else:
    ink += 7
  page = i

print(ink)