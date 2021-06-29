from collections import deque
n,m=0,0
board = list()
dir = [
    [0,1],
    [1,0],
    [-1,0],
    [0,-1]
]
def in_range(x:int,y:int):
    return 0<=x<n and 0<=y<m

def DFS(x:int,y:int,visited):
    visited[x][y]=True
    for i in range(4):
        dx = x +dir[i][0]
        dy = y+ dir[i][1]
        if in_range(dx,dy) and board[dx][dy]=='0' and not visited[dx][dy]:
            DFS(dx,dy,visited)

def solve_by_DFS():
    global n,m
    n,m=map(int,input().split())
    visited = [[False]*m for _ in range(n)]
    for i in range(n):
        board.append(input())
    ret=0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and board[i][j]=='0':
                DFS(i,j,visited)
                ret+=1
    print(ret)

def solve_by_BFS():
    global n,m
    n,m = map(int,input().split())
    visited = [[False]*m for _ in range(n)]
    for _ in range(n):
        board.append(input())
    ret=0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and board[i][j]=='0':
                ret+=1
                q = deque()
                q.append((i,j))
                visited[i][j]=True
                while q:
                    x,y = q.popleft()
                    for k in range(4):
                        dx = x+dir[k][0]
                        dy = y+dir[k][1]
                        if in_range(dx,dy) and board[dx][dy]=='0' and not visited[dx][dy]:
                            visited[dx][dy]=True
                            q.append((dx,dy))
    print(ret)


solve_by_BFS()
