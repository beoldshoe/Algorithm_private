'''def check(number) :
    n1 = float("inf")
    while(1) :
        if number % 10 == 0 :
            return 0
        else :
            if number % 10 > n1 :
                return 0
            else:
                if number // 10 == 0 :
                    return 1
                else : 
                    n1 = number % 10
                    number = number // 10 
                    
num = int(input())
cnt = 0
for i in range(10**num) :
    if check(i) == 1 :
        cnt += 1
    else : 
        pass
    
print(cnt%10007+1)'''

n = int(input())
dp = [1]*10
for i in range(1,n) :
    for j in range(1,10) :
        dp[j] += dp[j-1]
        
print(sum(dp)%10007)






                    
