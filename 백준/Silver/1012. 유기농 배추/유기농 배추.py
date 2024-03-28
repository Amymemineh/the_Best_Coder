import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, N, M, graph):
    if x < 0 or x >= N or y < 0 or y >= M:
        return False

    if graph[x][y] == 1:
        graph[x][y] = 0

        for i in range(4):
            dfs(x + dx[i], y + dy[i], N, M, graph)

        return True
    return False

T = int(input())
answers = []

for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0] * M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if dfs(i, j, N, M, graph):
                cnt += 1

    answers.append(cnt)

for ans in answers:
    print(ans)
