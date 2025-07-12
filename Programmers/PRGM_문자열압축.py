def solution(s):
    result = []
    
    if len(s) == 1:
        return 1
    for i in range(1, len(s)+1) :
        cnt = 1
        c = ''
        tmp = s[:i]
        for j in range(i, len(s)+i, i) :
            if tmp == s[j:j+i] :
                cnt += 1
            else :
                if cnt == 1:
                    c = c + tmp
                else :
                    c = c + str(cnt) + tmp
                cnt = 1
                tmp = s[j:j+i]
        result.append(len(c))
        
    return min(result)     