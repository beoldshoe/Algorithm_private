import sys

dict_info = {}
count = 0 

while (1) :
    word = sys.stdin.readline().rstrip()
    if word == '':
        break
    if word in dict_info :
        dict_info[word] += 1
        count += 1
    else :
        dict_info[word] = 1
        count += 1

sorted_list = sorted(dict_info.items(), key = lambda x : x[0])
for key, value in sorted_list :
    print('%s %.4f' %(str(key), round((value/count) * 100, 4)))



