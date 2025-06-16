N = int(input())

l = list(input())

current_B = 'R'
current_R = 'B'
count_B = 1
count_R = 1
for i in l :
    if current_B != i :
        if i == 'B' :
            count_B += 1
        current_B = i
    else :
        continue

for i in l :
    if current_R != i :
        if i == 'R' :
            count_R += 1
        current_R = i
    else :
        continue
count = min(count_R, count_B)
print(count)
    