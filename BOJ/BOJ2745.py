N, B = map(str, input().split())
num = list('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ')
l = list(N)
result = 0
leng = len(l)
for i in l :
    for n in range(len(num)) :
        if i == num[n] :
            result += int(B)**(leng-1)*n
            leng -= 1
            break
        
print(result)