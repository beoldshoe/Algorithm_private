# N = int(input())
# result = [11] * N

# check = list(map(int, input().split()))

# for i in range(N) :
#     a = check[i]
#     j = 0
#     while(1) :
#         if a == 0 :
#             k = j
#             while(1) : 
#                 if result[j] != 11 :
#                     j += 1
#                 else : 
#                     result[j] = i + 1
#                     j = k
#                     break
#             break
        
#         if result[j] > i + 1 :
#             a -= 1
#             j += 1
#         else :
#             pass
        
# print(*result)
# 틀린 코드 

n = int(input())

arr = list(map(int, input().split()))
answer = [0]*n

for i in range(n):   
    cnt = 0
    for j in range(n):
        if cnt == arr[i] and answer[j] == 0:
            answer[j] = i + 1
            break
        elif answer[j] == 0:
            cnt += 1
                
print(' '.join(map(str, answer)))
        
        
    