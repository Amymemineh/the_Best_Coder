n, m = map(int,input().split())
bang = [list(input()) for _ in range(n)]
visit = [[False] * m for _ in range(n)]
 
def dfs_garo(x,y):
    if x<0 or y<0 or x>=m or y>=n :
        return 0
    if visit[y][x] == False and bang[y][x]== '-':
        visit[y][x] = True
        bang[y][x] = 0
        return dfs_garo(x+1,y)
    return 0
 
def dfs_sero(x,y):
    if x<0 or y<0 or x>=m or y>=n :
        return 0 
    if visit[y][x] == False and bang[y][x]== '|':
        visit[y][x] = True
        bang[y][x] = 0
        return dfs_sero(x,y+1)
    return 0
 
count = 0
for i in range(n):
    for j in range(m):
        if bang[i][j] == '-':
            count += 1
            dfs_garo(j,i)
        elif bang[i][j] == '|':
            count += 1
            dfs_sero(j,i)
print(count)