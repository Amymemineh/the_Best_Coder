import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    input()
    a, b, c, d = map(int, input().split())
    total = a * b * c
    cut = 0
    while True:
        if cut == d: break
        a, b, c = sorted([a, b, c])
        total -= a * b
        c -= 1
        cut += 1
   
    print(total)
