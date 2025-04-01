n = int(input())
dp = [0] * (n+1)
for i in range(1, n+1) :
    if i == 1 or i == 3 :
        dp[i] = 100000
    elif i == 2 :
        dp[i] = 1
    elif i == 5 :
        dp[i] = 1
    elif i == 4 :
        dp[i] = 2
    elif i == 8 :
        dp[i] = 4
    else :
        if dp[i-5] > dp[i-2] :
            dp[i] = dp[i-2] + 1
        else :
            dp[i] = dp[i-5] + 1

if dp[n] == 100000 :
    dp[n] = -1
print(dp[n])