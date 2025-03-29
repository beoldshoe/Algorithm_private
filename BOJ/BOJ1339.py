# N = int(input())
# dic = {}
# char_list = []
# for _ in range(N) :
#      st = input()
#      char_list.append(st)
#      st = list(st)
#      for i in range(len(st)) :
#         if st[i] in dic.keys() :
#             if dic[st[i]] < len(st)-1-i :
#                 dic[st[i]] = len(st)-1-i 
#         else :
#             dic[st[i]] = len(st)-1-i 
# sorted_list = sorted(dic.items(), key=lambda x:x[1])
# num = 9

# while(1) :
#     item = sorted_list.pop()
#     dic[item[0]] = num
#     num -= 1
#     if len(sorted_list) == 0 : break
    
# cnt = 0
# ch = ''
# for char in char_list :
#     for c in char :
#         c = str(dic[c])
#         ch += c
#     cnt += int(ch)
#     ch = ''

# print(cnt)
# 처음에 생각했던 코드


N = int(input())
dic = {}
char_list = []
for _ in range(N) :
     st = input()
     char_list.append(st)
     st = list(st)
     for i in range(len(st)) :
        if st[i] in dic.keys() :
            dic[st[i]] += 10**(len(st)-1-i)
        else :
            dic[st[i]] = 10**(len(st)-1-i)
sorted_list = sorted(dic.items(), key=lambda x:x[1])
num = 9

while(1) :
    item = sorted_list.pop()
    dic[item[0]] = num
    num -= 1
    if len(sorted_list) == 0 : break
    
cnt = 0
ch = ''
for char in char_list :
    for c in char :
        c = str(dic[c])
        ch += c
    cnt += int(ch)
    ch = ''

print(cnt)