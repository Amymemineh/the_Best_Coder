import sys
input = sys.stdin.readline

n = int(input())
cnt = n
for _ in range(n):
    text = input().rstrip()
    stack = []

    for s in text:
        if stack and stack[-1] == s:
            stack.pop()
        else:
            stack.append(s)

    if stack:
        cnt -= 1
print(cnt)