def solution(id_list, report, k):
    idx = {}
    for i in range(len(id_list)) :
        c = id_list[i]
        idx[c] = 0
        idx[c] = i
        
    report = set(report)
    
    ed = {}
    
    for i in report :
        if i.split()[1] in ed.keys() :
            ed[i.split()[1]] += 1
        else :
            ed[i.split()[1]] = 1
            
    result = [0] * len(id_list)
    
    for i in report :
        if ed[i.split()[1]] >= k :
            id = idx[i.split()[0]]
            result[id] += 1
    return result