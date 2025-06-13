N = int(input())
tips = []
for _ in range(N) :
    tip = int(input())
    tips.append(tip)
    
tips.sort(reverse=True)
result = 0
for i in range(len(tips)) :
    r = tips[i] - ((i+1) - 1)
    if r < 0 :
        r = 0
    result += r


print(result)