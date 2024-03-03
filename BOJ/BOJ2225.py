N, K = map(int, input().split())

dp = [1]*(N+1)

for i in range(K-1) :
    for j in range(N+1) :
        if j == 0 :
            dp[j] = 1
        else :
            dp[j] = dp[j-1] + dp[j]
            
print(dp[N]%1000000000)

