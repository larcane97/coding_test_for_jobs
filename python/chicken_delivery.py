import itertools 
def distance(x,y):
    return abs(x[0]-y[0])+abs(x[1]-y[1])

n,m= map(int,input().split())
board=[]
for _ in range(n):
    board.append(list(map(int,input().split())))

house=[]
chicken=[]
for i in range(n):
    for j in range(n):
        if board[i][j]==1:
            house.append([i,j])
        elif board[i][j]==2:
            chicken.append([i,j,0])

answer=99999
for c in itertools.combinations(chicken,m):
    tmp_answer=0
    for i in range(len(house)):
        tmp=99999
        for j in range(len(c)):
            tmp = min(tmp,distance(house[i],c[j]))
        tmp_answer +=tmp
    answer = min(answer,tmp_answer)
print(answer)            
            
