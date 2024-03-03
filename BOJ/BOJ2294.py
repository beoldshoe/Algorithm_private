import sys

n, k = map(int, sys.stdin.readline().split())
coin = []

for _ in range(n) :
    c = int(input())
    coin.append(c)
    
dp = [0] * (k+1)
            
for i in range(1, k+1) :
    for j in coin :
        if i == j :
            dp[i] = 1
            
for i in range(1, k+1) :
    if dp[i] != 1 :
        check=[]
        for j in coin :
            if i-j<0 :
                pass
            else :
                if dp[i-j] != 0 :
                    check.append(dp[i-j])
                
        if len(check) != 0 :
            m = min(check)
            dp[i] = m+1
                     
if dp[k] == 0 :
    print(-1)
else :
    print(dp[k])         