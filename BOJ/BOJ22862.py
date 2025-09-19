N, K = map(int, input().split())

S = list(map(int, input().split()))

hol = 0
jjack = 0
result = 0
left, right = 0, 0

while(1) :
    if hol < K :
        if S[right] % 2 != 0 :
            hol += 1
            right += 1
        else : 
            jjack += 1
            right += 1
            result = max(result, jjack)
    else :
        if S[right] % 2 !=0 :
            hol += 1
            if S[left] % 2 !=0 :
                hol -= 1
                left += 1
                right += 1
            else :
                left += 1
                jjack -= 1
        else :
            jjack += 1
            right += 1
            result = max(result, jjack)
            
    if right == N :
        break
            
print(result)
        
        