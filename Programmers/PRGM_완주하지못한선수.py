# def solution(participant, completion):
#     check = 0
#     answer = ''
#     check_list = []
#     for i in range(len(completion)) :
#         check_list.append(0)
        
#     for i in range(len(participant)) :
#         check = 0
#         for j in range(len(completion)) :
#             if participant[i] == completion[j] and check_list[j] == 0: 
#                 check_list[j] = 1
#                 check = 1
#                 break
#         if check == 0 :
#             answer = participant[i]
#     return answer
# 시간 초과 뜬 코드

from collections import defaultdict

def solution(participant, completion):
    dic = defaultdict(int)
    
    for i in participant :
        dic[i] += 1
        
    for i in completion :
        dic[i] -= 1
        
    for i in dic.keys() :
        if dic[i] == 1 :
            return i
            