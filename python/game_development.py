import sys

def in_range(x,y):
  return 0<=x<n and 0<=y<n

dir=[[-1,0],[0,1],[1,0],[0,-1]]
n,m = map(int,input().split())
x,y,d = map(int,input().split())
visited = [[False]*m for _ in range(n)]
board=list()
for _ in range(n):
  board.append(list(map(int,input().split())))

ret=0
while True:
  move = False
  for _ in range(4):
    d -=1
    if d<0: d=3
    dx = x + dir[d][0]
    dy = y + dir[d][1]
    if in_range(dx,dy) and visited[dx][dy]==False and board[dx][dy]==0:
      visited[dx][dy]=True
      ret+=1
      x,y = dx,dy
      move=True
      break
  if move==False:
    dx = x -dir[d][0]
    dy = y -dir[d][1]
    if in_range(dx,dy) and board[dx][dy]==0:
      x,y=dx,dy
    else:
      break
  else:
    move=False
print(ret)
  

