DIV=796796
dp = [-1]*1001
n =int(input())
dp[1]=1
dp[2]=3
for i in range(3,n+1):
    dp[i]=(dp[i-2]*2+dp[i-1])%DIV
print(dp[n])

