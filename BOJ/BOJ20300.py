N = int(input())

l = list(map(int, input().split()))
sum = 0

l.sort()
result = 0
if N % 2 == 0 :
    for i in range(N//2) :
        if result < l[i] + l[N-i-1] :
            result = l[i] + l[N-i-1]
else :
    result = l[-1]
    for i in range(N//2) :
        if result < l[i] + l[N-i-2] :
            result = l[i] + l[N-i-2]

print(result)