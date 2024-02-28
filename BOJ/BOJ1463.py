n = int(input())

dp = [0] * (n+1)

for i in range(1, n+1) :
    if i == 1 :
        dp[i] = 0
    elif i == 2 :
        dp[i] = 1
    elif i == 3 :
        dp[i] = 1
    else :
        check = []
        if i % 3 == 0 :
            check.append(dp[i//3])
        if i % 2 == 0 :
            check.append(dp[i//2])
        check.append(dp[i-1])
        
        dp[i] = min(check)+1
        
print(dp[n])
            
    