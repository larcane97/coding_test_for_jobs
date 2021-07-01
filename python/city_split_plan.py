class disjoint:
    def __init__(self,n):
        self.parent= [i for i in range(n+1)]
        self.rank=[0]*(n+1)

    def find(self,u):
        if self.parent[u]!=u:
            self.parent[u]=self.find(self.parent[u])
        return self.parent[u]
    def union(self,u,v):
        u=self.find(u)
        v=self.find(v)
        if u==v:return False
        if self.rank[u] > self.rank[v]:
            u,v=v,u
        self.parent[v]=u
        if self.rank[u]==self.rank[v]:
            self.rank[u]+=1
        return True


n,m=map(int,input().split())
edges=[]
for _ in range(m):
    a,b,cost=map(int,input().split())
    edges.append((cost,a,b))
edges.sort()
ds=disjoint(n)
ret=0
max_cost=0
for i in edges:
    if ds.union(i[1],i[2]):
        ret+=i[0]
        max_cost=max(max_cost,i[0])
ret-=max_cost
print(ret)

