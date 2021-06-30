import sys
def calc_length(h,heights):
    ret=0
    for i in heights:
        if i-h>0:
            ret +=i-h
    return ret
n,m = map(int,sys.stdin.readline().rstrip().split())
heights = list(map(int,sys.stdin.readline().rstrip().split()))
left,right = 0,int(2e+10)+1
ret=-1
while left<=right:
    mid = (left+right)//2
    length=calc_length(mid,heights)
    if length<m:
        right=mid-1
    else:
        ret=max(ret,mid)
        left=mid+1
print(ret)
    



