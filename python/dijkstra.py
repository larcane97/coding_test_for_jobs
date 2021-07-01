import heapq
import sys
input = sys.stdin.readline
INF=987654321

n,m=map(int,input().split())
start=int(input())
graph= [[] for _ in range(n+1)]
distance = [INF]*(n+1)

for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))



def dijkstra(start):
    pq=[]
    heapq.heappush(pq,(0,start))
    distance[start]=0
    while pq:
        dis,here=heapq.heappop(pq)
        if distance[here] <dis:
            continue
        for there in graph[here]:
            cost = there[1]+dis
            if cost<distance[there[0]]:
                distance[there[0]]=cost
                heapq.heappush(pq,(cost,there[0]))

dijkstra(start)

for i in range(1,n+1):
    if distance[i]==INF:
        print("INFINITY")
    else:
        print(distance[i])