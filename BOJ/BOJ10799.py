in_value = input()
in_value = in_value.replace('()', '-')
check_list = []
v = 1
result = 0
cnt = 0

for i in in_value :
    if i == '(' :
        check_list.append(v)
        v += 1
    elif i == ')' :
        a = check_list.pop()
        cnt += 1
    elif i == '-' :
        result += len(check_list)

            
print(result + cnt)