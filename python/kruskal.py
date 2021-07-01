def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]
def union_parent(parent,rank,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a==b:return False
    if rank[a]>rank[b]:
        a,b=b,a
    parent[b]=a
    if rank[a]==rank[b]:
        rank[a]+=1
    return True

v,e=map(int,input().split())
parent=[i for i in range(v+1)]
rank=[1 for _ in range(v+1)]

edges=[]
ret=0

for _ in range(e):
    a,b,cost=map(int,input().split())
    edges.append((cost,a,b))
edges.sort()

for i in edges:
    if union_parent(parent,rank,i[1],i[2]):
        ret+=i[0]
print(ret)

