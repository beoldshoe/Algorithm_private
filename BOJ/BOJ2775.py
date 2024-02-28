T = int(input())

for _ in range(T) :
    k = int(input())
    n = int(input())
    
    dp = []
    for i in range(n) :
        dp.append(i+1)
    
    for i in range(1, k+1) :
        for j in range(n) :
            if j>0 :
                dp[j] += dp[j-1]
            else :
                pass
            
    print(dp[n-1])
        