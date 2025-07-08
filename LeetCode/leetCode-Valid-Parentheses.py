class Solution:
    def isValid(self, s: str) -> bool:
        s = list(s)
        stack = []
        for i in range(len(s)) :
            if s[i] == '(' or s[i] == '[' or s[i] == '{' :
                stack.append(s[i])
            elif s[i] == ')' :
                if s[i-1] == '(' :
                    if len(stack) != 0 :
                        stack.pop()
                    else :
                        return False
                else :
                    if len(stack) != 0 :
                        if stack.pop() == '(' :
                            continue
                        else :
                            return False
                    else :
                        return False
            elif s[i] == ']' :
                if s[i-1] == '[' :
                    if len(stack) != 0 :
                        stack.pop()
                    else :
                        return False
                else :
                    if len(stack) != 0 :
                        if stack.pop() == '[' :
                            continue
                        else :
                            return False
                    else :
                        return False
            elif s[i] == '}' :
                if s[i-1] == '{' :
                    if len(stack) != 0 :
                        stack.pop()
                    else :
                        return False
                else :
                    if len(stack) != 0 :
                        if stack.pop() == '{' :
                            continue
                        else :
                            return False
                    else :
                        return False

        if len(stack) != 0 :
            return False
        else :
            return True

        