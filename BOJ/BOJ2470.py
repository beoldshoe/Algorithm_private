N = int(input())
li = list(map(int,input().split()))

li.sort()

left, right = 0, N-1
result = 10000000000
res = []
while(1) :
    if li[left] < 0 :
        if abs(li[left]) >= abs(li[right]) :
            if result > abs(li[left] + li[right]) :
                result = abs(li[left]+li[right])
                res = [li[left], li[right]]
            left += 1

        else :
            if result > abs(li[left] + li[right]) :
                result = abs(li[left]+li[right])
                res = [li[left], li[right]]
            right -= 1
            
    else :
        if result > abs(li[left] + li[left+1]) :
            result = abs(li[left]+li[left+1])
            res = []
            res = [li[left], li[left+1]]
            right -= 1
        break
        
    if left == right :
        break
    
res.sort()
print(*res)