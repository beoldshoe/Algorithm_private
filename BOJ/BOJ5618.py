n = int(input())

num = list(map(int, input().split()))

m = min(num)

for i in range(1, m+1) :
    check = 0
    for j in num :
        if j % i != 0 :
            check = 1
            break
        else :
            continue

    if check == 0 :
        print(i)