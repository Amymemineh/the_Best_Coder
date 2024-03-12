n = int(input())
game = [list(map(int, input().split())) for _ in range(n)]
visit = [[False] * n for _ in range(n)]
 
def dfs(x,y):
    if x>=n or y>=n:
      return False
    i = game[x][y]
    if i == -1:
      print("HaruHaru")
      exit(0)
    
    if not visit[x][y]:
      visit[x][y] = True
      dfs(x+i, y)
      dfs(x, y+i)

dfs(0,0)
print("Hing")