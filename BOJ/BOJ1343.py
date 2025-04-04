s = list(input())
a = ''
cnt = 0
result = ''

for i in s :
    if i == '.' :
        if cnt != 0 :
            if cnt % 4 == 0 :
                l = cnt // 4
                result += 'AAAA'*l
            elif cnt % 4 == 2 :
                l = cnt // 4
                result += 'AAAA'*l
                result += 'BB'
            else :
                result = '-1'
                break
            result += '.'
        else : 
            result += '.'
        cnt = 0
    else :
        cnt += 1
if cnt != 0 :
    if cnt % 4 == 0 :
        l = cnt // 4
        result += 'AAAA'*l
    elif cnt % 4 == 2 :
        l = cnt // 4
        result += 'AAAA'*l
        result += 'BB'
    else :
        result = '-1'
        
print(result)