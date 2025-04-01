s = input()
s_list = list(s)
dic = {}
for i in s_list :
    if i in dic.keys() :
        dic[i] += 1
    else :
        dic[i] = 1

l = sorted(dic.items(), key=lambda x : x[0])
result = ''
mid = ''
cnt = 0
for i in l :
    if i[1] % 2 == 1 :
        cnt += 1
        mid = i[0]
        if cnt >= 2 :
            print("I'm Sorry Hansoo")
            exit()

for i in l :
    result += (i[0] * (i[1] // 2))

print(result + mid + result[::-1])  

# import collections
# import sys

# word = sys.stdin.readline().rstrip()
# check_word = collections.Counter(word)
# cnt = 0
# result = ''
# mid = ''
# for k, v in list(check_word.items()):
#     if v % 2 == 1: #홀수라면
#         cnt += 1
#         mid = k #중간에 들어갈 값으로 저장
#         if cnt >= 2: #홀수가 2개이상이면 팰린드롬이 될 수 없다!!
#             print("I'm Sorry Hansoo")
#             exit()

# for k, v in sorted(check_word.items()): #정렬을 통해 사전순으로 for문을 돌게함
#     result += (k * (v // 2)) #정확히 절반으로 나뉜 문자열을 만들어야 하므로 현재 갯수를 2로 나눠줌
# print(result + mid + result[::-1]) # 앞+중간+뒤 를 더해 문자열 출력
# 출처 : 
# https://velog.io/@rovna/%EB%B0%B1%EC%A4%80-1213%EB%B2%88-%ED%8C%B0%EB%A6%B0%EB%93%9C%EB%A1%AC-%EB%A7%8C%EB%93%A4%EA%B8%B0