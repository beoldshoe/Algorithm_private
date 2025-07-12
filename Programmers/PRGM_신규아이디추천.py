def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    check = ['0','1','2','3','4','5','6','7','8','9','-','_','.']
    for i in new_id :
        if i.islower() or i in check :
            answer += i
    while '..' in answer :
        answer = answer.replace('..', '.')
                
    if answer[0] == '.' and len(answer) > 1 :
        answer = answer[1:]
    else :
        answer
            
    if answer[-1] == '.' :
        answer = answer[:-1]
    else :
        answer
    
    if answer == '' :
        answer = 'a'
    else :
        answer
        
    if len(answer) >= 16 :
        answer = answer[:15]
        if answer[-1] == '.' :
            answer = answer[:-1]
                
    if len(answer) <=3 :
        answer = answer + answer[-1] * (3-len(answer))
                    
    return answer
        
                