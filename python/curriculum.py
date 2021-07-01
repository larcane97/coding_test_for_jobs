from collections import deque
import copy

v=int(input())
indegree=[0]*(v+1)
adj=[[] for _ in range(v+1)]
time=[0]*(v+1)
for i in range(1,v+1):
    data=list(map(int,input().split()))
    time[i]=data[0]
    for x in data[1:-1]:
        indegree[i]+=1
        adj[x].append(i)

def topological_sort():
    result=copy.deepcopy(time)
    q=deque()

    for i in range(1,v+1):
        if indegree[i]==0:
            q.append(i)

    while q:
        here=q.popleft()

        for i in adj[here]:
            result[i]=max(result[i],result[here]+time[i])
            indegree[i]-=1
            if indegree[i]==0:
                q.append(i)

    for i in range(1,v+1):
        print(result[i])

topological_sort()
