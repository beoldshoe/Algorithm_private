import math

N= int(input())
dp = [0] * (N+1)

for i in range(1, N+1) :
    n = int(math.sqrt(i))
    if i - n**2 == 0 :
        dp[i] = 1
    else :
        mx = 1000000000
        n = int(math.sqrt(i))
        for j in range(1, n+1) :
            j = j**2
            mx = min(mx, dp[j] + dp[i-j])
        dp[i] = mx

print(dp[-1])
