from collections import deque

N = int(input())

num = deque(map(int, input().split()))

q = deque()

for i in range(N) :
    q.append(i+1)

list = []
check = 0
while(1) : 
    a = q.popleft()
    b = num.popleft()
    list.append(a)
    if check == 1:
        num.reverse()
        q.reverse()
        check = 0
    if len(q) == 0 : break
    if b > 0 : 
        for _ in range(b-1) :
            num.append(num.popleft())
            q.append(q.popleft())
    else :
        b = -b
        num.reverse()
        q.reverse()
        for _ in range(b-1) :
            num.append(num.popleft())
            q.append(q.popleft())
        check = 1

print(*list)
        

    