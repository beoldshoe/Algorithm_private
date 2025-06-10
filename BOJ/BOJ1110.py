N = input()

if int(N) < 10 :
    N = '0' + N
    N = list(str(N))
else :
    N = list(N)

c1 = N[0]
c2 = N[1]
cnt = 0
while(1) :
    first = N[0]
    second = N[1]
    sum = (int(N[0]) + int(N[1]))%10

    N[0] = N[1]
    N[1] = str(sum)
    cnt += 1
    
    if c1 == N[0] and c2 == N[1] :
        print(cnt)
        break
