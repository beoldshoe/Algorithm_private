n = input()

result = list()

for i in range(len(n)) :
    if ord(n[i])>=65 and ord(n[i])<=90 : # 문자
        result.append(ord(n[i])-64)
    elif ord(n[i])>=48 and ord(n[i])<=57 : # 숫자
        result.append(ord(n[i])-21)
    else :
        continue
    
result.sort()
count = 0
calcul = 0

for i in range(len(n)) :
    if result[i]>=27 and result[i]<=36 : # 숫자
        result[i] = chr(result[i]+21)
        count = count+1
        calcul = calcul + int(result[i])
    elif result[i]>=1 and result[i] <=26 : # 문자
        result[i] = chr(result[i]+64)
    else :
        continue
for j in range(count):
    result.pop()
calcul = str(calcul)
result.append(calcul)
print(''.join(result))