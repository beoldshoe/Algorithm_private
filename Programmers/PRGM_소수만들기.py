import math

def solution(nums):
    
    def isprime(num) :
        for i in range(2, int(math.sqrt(num))+1) :
            if num % i == 0 :
                return False
        return True
    
    l = len(nums)
    number = 0
    cnt = 0
    for i in range(l-2) :
        for j in range(i+1, l-1) :
            for k in range(j+1, l) :
                number = nums[i] + nums[j] + nums[k]
                if isprime(number) :
                    cnt += 1
                    
    return cnt
                
# print(solution([1,2,7,6,4]))    