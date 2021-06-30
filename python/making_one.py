import sys
INF = 987654321
sys.setrecursionlimit(INF)
dp=[-1]*30001
x = int(input())
def solve(x:int):
    if x==1 : return 0
    if dp[x] !=-1: return dp[x]
    ret=solve(x-1)+1
    if x%5==0:
        ret = min(ret,solve(x//5)+1)
    if x%3==0:
        ret = min(ret,solve(x//3)+1)
    if x%2==0:
        ret = min(ret,solve(x//2)+1)
    return ret
print(solve(x))
        



