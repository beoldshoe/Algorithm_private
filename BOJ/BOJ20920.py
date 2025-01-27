N, M = map(int, input().split())

wd = {}
w_list = []

for _ in range(N) :
    w = input()
    if len(w) < M : continue
    else : 
        if w not in wd.keys() :
            wd[w] = 1
        else :
            wd[w] += 1
            
for x in wd.keys() :
    w_list.append([x, len(x), wd.get(x)])
    
sorted_w_list = sorted(w_list, key=lambda x: (-x[2], -x[1], x[0]))
            
    
for x in sorted_w_list :
    print(x[0])
        
    
# import sys
# input = sys.stdin.readline

# N, M = map(int, input().rstrip().split()) # 단어 개수, 단어 길이
# word_lst = {} # 딕셔너리

# for _ in range(N):
#     word = input().rstrip()
    
#     if len(word) < M: # 단어가 M미만인 경우
#         continue
#     else: # 단어가 M이상인 경우
#         if word in word_lst: # 단어가 있는 경우
#             word_lst[word] += 1
#         else: # 단어가 없는 경우
#             word_lst[word] = 1

# word_lst = sorted(word_lst.items(), key = lambda x : (-x[1], -len(x[0]), x[0])) # x[0] = 단어, x[1] = 단어 빈도수
# # -x[1] = 자주 나오는 단어 앞에 배치
# # -len(x[0]) = 단어 길이 길수록 앞에 배치
# # x[0] = 단어 사전 순 정렬

# for i in word_lst:
#     print(i[0])  