N, L = map(int, input().split())

location = list(map(int,input().split()))

location.sort()
a = location[0]
cnt = 1
check = 0
for i in range(1, len(location)) :
    if check == 1 : # 테이프가 감쌀 수 있는 부분 완료
        a = location[i]
        cnt += 1
        check = 0
        continue # 다음으로 넘어가기
    if location[i]-a < L-1 : # 테이프가 뒤의 위치도 더 감쌀 수 있을 때
        cnt = cnt
    elif location[i]-a == L-1 : # 테이프가 감쌀 수 있는 마지막 위치를 감쌀 때
        check = 1
    else : # 테이프가 딱 한 위치만 감쌀 수 있을 때
        cnt += 1
        a = location[i]
    
print(cnt)