N = int(input())
m_num_list = []
num_list = []
zero = []
for _ in range(N) :
    num = int(input())
    if num < 0 :
        m_num_list.append(num)
    elif num > 1  :
        num_list.append(num)
    else :
        zero.append(num)
        
m_num_list.sort(reverse=True)
num_list.sort()
check = 0
cnt = 0
if len(m_num_list) != 0 :
    while(1) :
        if check == 0 and len(m_num_list) <= 1 :
            break
        
        a = m_num_list.pop()   
        if check == 0 :
            check = a
        else :
            cnt += a*check
            check = 0

    z_check = 0
    if len(m_num_list) > 0 :
        for i in zero :
            if i == 0 :
                m_num_list.pop()
                z_check = 1
                break
        if z_check == 0 :
            cnt += m_num_list.pop()
        
    
check = 0
if len(num_list) != 0 :
    while(1) :
        if check == 0 and len(num_list) <= 1 :
            break  
         
        a = num_list.pop()   
        if check == 0 :
            check = a
        else :
            cnt += a*check
            check = 0
  

    if len(num_list) > 0 :
        cnt += num_list.pop()
    
if len(zero) != 0 :
    for i in zero :
        cnt += i
        
if len(m_num_list) > 0 :
    cnt += m_num_list.pop()
        

    
print(cnt)
    
