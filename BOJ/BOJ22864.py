A, B, C, M = map(int, input().split())

result = 0
firodo = 0
for i in range(24) :
    if firodo + A > M :
        firodo -= C
        if firodo < 0 :
            firodo = 0
    else :
        firodo += A
        result += B

print(result)