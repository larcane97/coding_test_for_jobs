from collections import deque

def in_range(x,y):
    return 0<=x<n and 0<=y<m
dir =[
    [0,1],
    [1,0],
    [-1,0],
    [0,-1]
]
n,m = map(int,input().split())
visited= [[False]*m for _ in range(n)]
board=list()
for _ in range(n):
    board.append(input())

q= deque()
visited[0][0]=True
q.append((0,0,1))

while q:
    x,y,dis = q.popleft()
    if x == n-1 and y == m-1:
        print(dis)
        break
    for i in range(4):
        dx = x +dir[i][0]
        dy = y +dir[i][1]
        if in_range(dx,dy) and board[dx][dy]=='1' and not visited[dx][dy]:
            visited[dx][dy]=True
            q.append((dx,dy,dis+1))
