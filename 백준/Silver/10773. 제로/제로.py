import sys
input = sys.stdin.readline

k = int(input())
num = []

for i in range(k):
  su = int(input())
  if su == 0: num.pop()
  else: num.append(su)

print(sum(num))