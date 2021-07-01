from collections import deque

v,e=map(int,input().split())
indegree= [0]*(v+1)
adj=[[] for _ in range(v+1)]
for _ in range(e):
    a,b=map(int,input().split())
    indegree[b]+=1
    adj[a].append(b)

def topological_sort():
    result=[]
    q=deque()
    for i in range(1,v+1):
        if indegree[i]==0:
            q.append(i)
    
    while q:
        a = q.popleft()
        result.append(a)
        for i in adj[a]:
            indegree[i]-=1
            if indegree[i]==0:
                q.append(i)
    for i in result:
        print(i,end=' ')
topological_sort()
