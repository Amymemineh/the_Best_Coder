import sys
input = sys.stdin.readline
n = int(input())
plugs = 0

for plug in range(n):
    plug = int(input())
    plugs += plug

answer = plugs-n+1
print(answer)
