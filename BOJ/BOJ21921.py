N, X = map(int, input().split())

people = list(map(int, input().split()))
# s = 0
# cnt = 1
# for i in range(N-X+1) :
#     l = sum(people[i:i+X])
#     if s < l :
#         s = l
#         cnt = 1
#     elif s == l :
#         cnt += 1
# if s == 0 :
#     print('SAD')
# else :  
#     print(s)
#     print(cnt)

value = sum(people[:X])
s = value
cnt = 1

for i in range(X, N) :
    value += people[i]
    value -= people[i-X]
    
    if value > s :
        s = value
        cnt = 1
    elif value == s :
        cnt += 1
        
if s == 0 :
    print('SAD')
else :  
    print(s)
    print(cnt)