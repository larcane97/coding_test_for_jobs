INF=987654321
n,m=map(int,input().split())
adj= [[INF]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    adj[i][i]=0
for _ in range(m):
    a,b=map(int,input().split())
    adj[a][b]=1
    adj[b][a]=1

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            adj[i][j]=min(adj[i][j],adj[i][k]+adj[k][j])

x,k=map(int,input().split())
ret= adj[1][k]+adj[k][x]
if ret>=INF:
    print(-1)
else:
    print(ret)
