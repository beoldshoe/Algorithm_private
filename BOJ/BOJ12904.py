S = input()
T = list(input())
ch = ''
while(1) :
    if len(T) == len(S) :
        for i in T :
            ch += i
            
        if ch == S :
            print(1)
            break
        else :
            print(0)
            break
        
    check = T.pop()

    if check == 'A' :
        T = T
    else :
        T.reverse()
        
        
    
        