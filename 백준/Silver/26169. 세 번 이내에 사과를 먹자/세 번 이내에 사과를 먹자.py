dx=[-1,1,0,0]
dy=[0,0,-1,1]
board=[list(map(int,input().split())) for _ in range(5)]
visited=[[False]*5 for _ in range(5)]
r,c=map(int,input().split())
def dfs(x,y,cnt,apple):
  visited[x][y]=True
  if board[x][y]==1:
    apple+=1
  if apple>=2:
    return 1
  if cnt>2:
    visited[x][y]=False
    return 0
  for d in range(4):
    newx=x+dx[d]
    newy=y+dy[d]
    if 0<=newx<5 and 0<=newy<5:
      if board[newx][newy]!=-1 and visited[newx][newy]==False:
        if dfs(newx,newy,cnt+1,apple)==1:
          return 1
  visited[x][y]=False
  return 0
print(dfs(r,c,0,0))