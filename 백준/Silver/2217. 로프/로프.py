import sys
input = sys.stdin.readline

n = int(input())
rope = sorted([int(input()) for _ in range(n)])
answer = 0

for i in range(n):
  weight = rope[i] * (n-i)
  if weight > answer:
    answer = weight

print(answer)