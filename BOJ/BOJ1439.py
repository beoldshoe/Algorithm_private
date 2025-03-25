S = input()

S_list = list(S)

check = S_list[0]
cnt = 1
for i in range(1, len(S_list)) :
    if check != S_list[i] :
        cnt += 1
        check = S_list[i]

print(cnt//2)