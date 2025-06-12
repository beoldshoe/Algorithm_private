import math

def isprime(num) :
    check = 0
    for i in range(2, int(math.sqrt(num)+1)) :
        if num % i == 0 :
            check = 1
            return False
        
    if check == 0 :
        return True

n = int(input())

for _ in range(n) :
    num = int(input())
    while(1) :
        if num == 0 or num == 1 :
            print(2)
            break
        if isprime(num) :
            print(num)
            break
        else :
            num += 1
        
