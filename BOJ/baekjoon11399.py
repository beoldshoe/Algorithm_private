n = int(input())

people_time = list(map(int, input().split()))

people_time.sort()

count = 0

for i in range(0, len(people_time)) :
    count = count + int(people_time[i]*(len(people_time)-i))
    
print(count)
