import sys

# 입력 받기
input = sys.stdin.readline
n = int(input())
rope = sorted([int(input()) for _ in range(n)])

# 최대 무게 계산
answer = max(rope[i] * (n - i) for i in range(n))

# 결과 출력
print(answer)
