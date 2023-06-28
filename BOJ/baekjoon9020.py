def is_sosu(num):
    for i in range(2, num):
        if num % i !=0:
            continue
        else:
            return 0
    return 1

def gold_partition(a,b):
    num_a = is_sosu(a)
    num_b = is_sosu(b)
    if (num_a == 1 and num_b == 1):
        a = a
        b = b
        print(a,b)
    else :
        a = a-1
        b = b+1
        gold_partition(a,b)

T = int(input())

for i in range(T) :
    n = int(input())
    first = n//2
    second = n//2
    gold_partition(first,second)
    
    
