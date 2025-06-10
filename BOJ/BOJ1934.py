import math

# def solution(A, B) :
#     def isprime(num) :
#         check = 0
#         for i in range(2, int(math.sqrt(num)) + 1) :
#             if num % i == 0 :
#                 check = 1
#                 return False
#         if check == 0 :
#             return True
    
#     result = 1 
#     if A % B == 0 :
#         return A
#     elif B % A == 0 :
#         return B
#     else :
#         i = 2
#         cnt = 0
#         while(1) :
#             if not isprime(i) :
#                 i += 1
#                 continue
#             if A % i == 0 and B % i == 0 :
#                 cnt += 1
#                 A = A // i
#                 B = B // i
#             elif A % i == 0 and B % i != 0 :
#                 A = A // i
#                 cnt += 1
#             elif A % i != 0 and B % i == 0 :
#                 B = B // i
#                 cnt += 1
#             else :
#                 result *= i ** cnt
#                 i += 1
#                 cnt = 0
#                 if A == 1 and B == 1 :
#                     break
                
#     return result

def solution(A, B) :
    result = A * B // math.gcd(A, B)
    
    return result

T = int(input())

for _ in range(T) :
    A, B = map(int, input().split())
    print(solution(A, B))

