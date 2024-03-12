n, new, p = map(int, input().split())
score_list = []
if n > 0: score_list = list(map(int, input().split()))

if len(score_list) >= p and new <= score_list[-1]:
  print(-1)
else:
  score_list.append(new)
  score_list.sort(reverse = True)
  print(score_list.index(new) + 1)