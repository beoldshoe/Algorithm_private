import sys

n, k = map(int, sys.stdin.readline().split())
check_list = set()  # 결과 리스트에 이미 담은 것인지 확인하기 위한 
result = []         # 결과 리스트
start = 0           # 일단 0부터 시작
cnt = 0             # 카운트

while(len(result) != n) :
    start = start + 1       # 현재 위치의 숫자 업데이트
     
    if start > n :          # 끝 숫자까지 갔을 때 1로 다시 업데이트
        start = 1
    
    if start in check_list :    # check_list 에 숫자가 있다면
        cnt = cnt
    else :
        cnt = cnt + 1           # 아니라면 카운트 ++1
        
    if cnt == k :               # k번째 숫자면
        cnt = 0
        check_list.add(start)   # check_list에 담기
        result.append(start)    # 결괴 리스트에 담기
        
print(str(result).replace('[', '<').replace(']', '>'))

