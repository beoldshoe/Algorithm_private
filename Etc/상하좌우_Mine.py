n = int(input())
moving = input().split()

recent = [1, 1] # 현재 위치를 [1,1]로 설정

for i in moving :
    if i == 'R' : # R이면 현재 위치의 y좌표 +1
        if recent[1] != n : 
            recent[1] = recent[1] + 1
        else :
            continue # 가장 끝(오른쪽)에 있으면 무시
    elif i == 'L' : # L이면 현재 위치의 y좌표 -1
        if  recent[1] != 1 :
            recent[1] = recent[1] - 1
        else :
            continue # 가장 끝(왼쪽)에 있으면 무시
    elif i == 'U' : # U이면 현재 위치의 x좌표 -1 
        if recent[0] != 1 :
            recent[0] = recent[0] - 1
        else :
            continue # 가장 끝(위쪽)에 있으면 무시
    else : # 나머지(D)면 현재 위치의 x좌표 +1
        if recent[0] != n :
            recent[0] = recent[0] + 1
        else : # 가장 끝(아래쪽)에 있으면 무시
            continue
    
print(recent[0], recent[1])

