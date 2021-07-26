def in_range(n,x,y):
    return x>0 and x<=n and y>0 and y<=n

dir=[
    [0,1],
    [-1,0],
    [0,-1],
    [1,0]]

def main():
    n = int(input())
    board = [[0]*(n+1) for _ in range(n+1)]
    k = int(input())
    for _ in range(k):
        a,b = map(int,input().split())
        board[a][b]=1

    l = int(input())
    direction = list()
    for _ in range(l):
        a,b = input().split()
        direction.append((int(a),b))

    snake=list()
    snake.append([1,1])
    cur_d = 0
    time=0
    while True:
        time+=1
        cx,cy = snake[-1]
        nx,ny = cx+dir[cur_d][0],cy+dir[cur_d][1]
        
        if not in_range(n,nx,ny) or [nx,ny] in snake:
            break

        snake.append([nx,ny])
        if board[nx][ny]!=1:
            snake.pop(0)
        else:
            board[nx][ny]=0
        
        # print('----------------------')
        # print('time: {},next move: ({},{})'.format(time,nx,ny))
        # print('snake :',snake)
        # print('----------------------')
        if len(direction)>0 and direction[0][0]==time:
            move = direction[0][1]
            direction.pop(0)
            if move=='D':
                cur_d -=1
                if cur_d<0:
                    cur_d=3
            else:
                cur_d +=1
                if cur_d>3:
                    cur_d=0
    print(time)
            





if __name__=="__main__":
    main()

