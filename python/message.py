import heapq
INF=987654321
n,m,start=map(int,input().split())
adj= [[] for _ in range(n+1)]
distance= [INF]*(n+1)
pq=[]

for _ in range(m):
    a,b,c=map(int,input().split())
    adj[a].append((b,c))

heapq.heappush(pq,(0,start))
distance[start]=0
while pq:
    dist,here= heapq.heappop(pq)
    if distance[here]<dist: continue
    
    for i in adj[here]:
        there = i[0]
        cost = i[1]
        if cost+dist<distance[there]:
            distance[there]=cost+dist
            heapq.heappush(pq,(cost+dist,there))
            

distance= [distance[i] for i in range(1,n+1) if distance[i] < INF]
print(len(distance)-1,max(distance))