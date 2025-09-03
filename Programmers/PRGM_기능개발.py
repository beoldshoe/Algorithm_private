def solution(progresses, speeds) :
    l = len(progresses)
    days = []
    for i in range(l) :
        a = (100 - progresses[i]-1)//speeds[i]
        days.append(a+1)
    answer = []
    
    compare = days[0]
    
    cnt = 1
    for i in range(1, len(days)) :
        if compare >= days[i] :
            cnt += 1
        else :
            answer.append(cnt)
            cnt = 1
            compare = days[i]
            
    answer.append(cnt)
            
            
    return answer
        