l = list(input())

def maximum(l) :
    result = ''
    m_stack = 0
    for i in l :
        if i == 'K' :
            if m_stack == 0 :
                result += '5'
            else :
                result += '5'
                for _ in range(m_stack) :
                    result += '0'
                m_stack = 0
        else :
            m_stack += 1

    if m_stack != 0 :
        for _ in range(m_stack) :
            result += '1'

    return result

def minimum(l) :
    result = ''
    m_stack = 0
    for i in l :
        if i == 'M' :
            m_stack += 1
        else :
            if m_stack != 0 :
                result += '1'
                for _ in range(m_stack-1) :
                    result += '0'
                result += '5'
                m_stack = 0
            else :
                result += '5'
    
    if m_stack != 0 :
        result += '1'
        for _ in range(m_stack-1) :
            result += '0'

    return result

maxi = maximum(l)
mini = minimum(l)
print(maxi)
print(mini)


