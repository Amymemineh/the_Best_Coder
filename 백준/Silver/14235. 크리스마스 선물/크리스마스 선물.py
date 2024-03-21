import sys
import heapq

input = sys.stdin.readline

n = int(input())
cnt = 0
present = []

for _ in range(n):
    a = list(map(int, input().split()))
    if a[0] != 0:
        cnt += a[0]
        for i in range(1, len(a)):
            heapq.heappush(present, -a[i])  # 음수로 넣어 최대 힙으로 사용
    else:
        if present:
            print(-heapq.heappop(present))  # 최대값을 꺼내어 양수로 출력
        else:
            print(-1)
