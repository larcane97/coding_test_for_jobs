n=int(input())
fear=list(map(int,input().split()))
fear.sort()
print(fear)
ret=0
cur=0
sel=0
while cur<n:
    sel+=1
    if fear[cur]<=sel:
        ret+=1
        sel=0
    cur+=1
print(ret)
        
