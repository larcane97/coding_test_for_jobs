def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,rank,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if rank[a]>rank[b]:
        a,b=b,a
    parent[b]=a
    if rank[a]==rank[b]:
        rank[a]+=1
    return

v,e= map(int,input().split())
parent = [i for i in range(v+1)]
rank=[1 for _ in range(v+1)]

for i in range(e):
    a,b=map(int,input().split())
    union_parent(parent,rank,a,b)
print()
for i in range(1,v+1):
    print(find_parent(parent,i),end=' ')

        
        
