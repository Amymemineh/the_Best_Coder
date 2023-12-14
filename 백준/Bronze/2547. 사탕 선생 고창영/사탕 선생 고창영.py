import sys

input = sys.stdin.readline
t = int(input())


for _ in range(t):
    sys.stdin.readline().strip()
    n = int(input())
    cnt_list = []
    for _ in range(n):
        cnt_list.append(int(input()))
    if sum(cnt_list) % n == 0:
        print('YES')
    else:
         print('NO')
         