n = int(input())

cnt = 0
result = 0

for i in range(59) :
    if i // 10 == 3 :
        cnt += 1
    elif i % 10 == 3 :
        cnt += 1
    else :
        continue

for j in range(n+1) :
    if j % 10 == 3 :
        result += 60*60
    else :
        result += 60*cnt*2 - cnt*cnt
        
print(result)
