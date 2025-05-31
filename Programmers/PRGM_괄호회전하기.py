from collections import deque

def solution(s):
    s = deque(s)
    l = len(s)
    cnt = 0 
    while(1) :
        tmp = True
        stack = []
        if l == 0 : break
        for i in s :
            if i == '(' :
                stack.append('(')
            elif i == '[' :
                stack.append('[')
            elif i == '{' :
                stack.append('{')
            elif i == ')' :
                if len(stack) == 0 :
                    tmp = False
                    break
                if stack.pop() == '(' :
                    continue
                else :
                    tmp = False
                    break
            elif i == ']' :
                if len(stack) == 0 :
                    tmp = False
                    break
                if stack.pop() == '[' :
                    continue
                else :
                    tmp = False
                    break
            else :
                if len(stack) == 0 :
                    tmp = False
                    break
                if stack.pop() == '{' :
                    continue
                else :
                    tmp = False
                    break
                    
        if len(stack) != 0 :
            tmp = False
               
            
        if tmp == True :
            cnt += 1
                
        s.append(s.popleft())
        l = l - 1
            
    return cnt