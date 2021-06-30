INF =987654321
dp = [INF]*10001
n,m=map(int,input().split())
s=set()
for _ in range(n):
    s.add(int(input()))

def calc(cur:int):
    if cur<0:return INF
    if dp[cur]!=INF:return dp[cur]
    if cur in s:
        dp[cur]=1
        return dp[cur]
    for v in s:
        dp[cur]=min(dp[cur],calc(cur-v)+1)
    return dp[cur]
print(calc(m))
    
    
    
