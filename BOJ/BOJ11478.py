S = str(input())
S_list = list(S)
S_set = set()
current_str = ''
for i in range(len(S_list)) :
    current_str = ''
    for j in range(i, len(S_list)) :
        current_str = current_str + S_list[j]
        S_set.add(current_str)

print(len(S_set))