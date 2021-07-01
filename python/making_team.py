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
ds=disjoint(n)
for _ in range(m):
    a,u,v=map(int,input().split())
    if a==0:
        ds.union(u,v)
    else:
        if ds.find(u)==ds.find(v):
            print("YES")
        else:
            print("NO")
    