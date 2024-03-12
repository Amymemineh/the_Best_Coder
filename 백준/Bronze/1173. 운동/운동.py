N, m, M, T, R = map(int, input().split())
exercise = 0
answer = 0
pulse = m

if M - m < T:
  print(-1)
else:
  while exercise < N:
    if pulse + T <= M:
      exercise += 1
      answer += 1
      pulse += T
    else:
      answer += 1
      pulse -= R                  
      if pulse < m:
        pulse = m
  
  print(answer)