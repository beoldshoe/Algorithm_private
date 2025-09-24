N, S = map(int, input().split())

li = list(map(int, input().split()))

l = 0
r = l + 1
tmp = li[l] + li[r]
leng = 100001
if li[l] >= S :
    print(1)
    exit()
while(1) :
    if tmp < S :
        r += 1
        if r == N :
            break
        tmp += li[r]
    else :
        leng = min(leng, r-l + 1)
        l += 1
        tmp -= li[l-1]
    if leng == 1 :
        break

if leng == 100001 :
    print(0)
else : print(leng)