N, C = map(int, input().split())

num_list = list(map(int, input().split()))

dict_info = {}
idx = 1
answer = ''

for num in num_list :
    if num in dict_info :
        dict_info[num][0] += 1
    else :
        dict_info[num] = [1, idx]
        idx += 1
        
sorted_num = sorted(dict_info.items(), key = lambda x: (-x[1][0], x[1][1]) )

for key, value in sorted_num :
    answer += (str(key) + ' ') * value[0]
    
print(answer[:-1])



