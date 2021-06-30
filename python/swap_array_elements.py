import heapq
n,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(lambda a: -1*int(a),input().split()))
heapq.heapify(a)
heapq.heapify(b)
for i in range(k):
    d1 = heapq.heappop(a)
    d2 = -heapq.heappop(b)
    heapq.heappush(a,d2)
    heapq.heappush(b,-d1)
print(sum(a))

    
