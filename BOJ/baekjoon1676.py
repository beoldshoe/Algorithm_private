def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result = result*i
    return result

N = int(input())
R = factorial_iterative(N)
count = 0

while R % 10 == 0 :
    R = R // 10
    count = count + 1
    
print(count)