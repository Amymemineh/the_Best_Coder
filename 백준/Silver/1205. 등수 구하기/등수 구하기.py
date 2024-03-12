n, new, p = map(int, input().split())
score_list = list(map(int, input().split())) if n > 0 else []

if len(score_list) >= p and new <= score_list[-1]:
  print(-1)
else:
  score_list = sorted(score_list + [new], reverse = True)
  print(score_list.index(new) + 1)