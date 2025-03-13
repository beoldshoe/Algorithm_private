# M, N, L = map(int, input().split())

# x_list = list(map(int, input().split()))

# x_list.sort()

# anmial_list = []
# for _ in range(N) :
#     x, y = map(int, input().split())
#     anmial_list.append((x,y))
# cnt = 0
# anmial_list.sort() 
# for i in anmial_list :
#     if i[1] > L : pass
#     for j in x_list :
#         if abs(i[0]-j) + i[1] <= L : 
#             cnt += 1
#             break
        
# print(cnt)
    
M, N, L = map(int, input().split())

x_list = list(map(int, input().split()))
animal_list = []
for _ in range(N) :
    x, y = map(int, input().split())
    animal_list.append((x,y))
cnt = 0
x_list.sort()

for i in animal_list :
    if(i[1]>L) :
        continue
    max = i[0]-i[1]+L
    min = i[0]+i[1]-L
    left, right = 0, M-1
    while left<=right :
        mid = (left+right)//2
        if x_list[mid] >=min and x_list[mid]<=max :
            cnt += 1
            break
        elif x_list[mid] < min :
            left = mid + 1
        else :
            right = mid - 1
print(cnt)
    