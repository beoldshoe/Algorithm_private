# N = int(input())

# xy = list(map(int,input().split()))

# xy_sort = sorted(xy)
# xy_set = set(xy_sort)

# print(xy_set)

# result = []
# cnt = 0
# for i in xy :
#     for j in xy_set :
#         if i > j : cnt+=1 
#     result.append(cnt)
#     cnt = 0
            
# print(*result)

import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr2 = sorted(list(set(arr)))
dic = {arr2[i] : i for i in range(len(arr2))}
for i in arr:
    print(dic[i], end = ' ')
        