n = int(input())

dp = [1] * 10
if n > 1 :
    for _ in range(n-1) :
        check = [0] * 10
        for i in range(10) :
            if i == 0 :
                check[i] = dp[i+1]
            elif i == 9 :
                check[i] = dp[i-1]
            else :
                check[i] = dp[i+1] + dp[i-1]
                
        dp = check
    
l = sum(dp)-dp[0]

print(l%1000000000)


    
