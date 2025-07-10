def solution(prices):
    answer = []
    for i in range(len(prices)) :
        cnt = 0
        for j in range(i+1, len(prices)) :
            if prices[i] <= prices[j] :
                cnt += 1
                if j == len(prices)-1 :
                    answer.append(cnt)
            else :
                cnt += 1
                answer.append(cnt)
                break
    answer.append(0)
    
    return answer