def solve(cur:int):
    if cur>=n: return 0
    if dp[cur]!=-1: return dp[cur]
    dp[cur]=max(solve(cur+1),solve(cur+2)+arr[cur])
    return dp[cur]

n=int(input())
arr=list(map(int,input().split()))
dp=[-1]*101

print(solve(0))



