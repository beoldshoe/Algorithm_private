N = int(input())
li = []
l = list(map(int, input().split()))
c = list(map(int, input().split()))
cost = []
for _ in range(len(c)):
    cost.append(0)
    

for i in range(len(c)-1) :
    li.append((c[i], l[i], i))
li = sorted(li, key=lambda x:(x[0], x[2]))

index = 10000000
temp_cost = 0
temp_lo = len(c)
for item in li :
    if item[2] < index :
        temp_cost = item[0]
        index = item[2]
    for i in range(index, temp_lo) :
        cost[i] = temp_cost
        temp_lo = index
    if index == 0 : break
result = 0   
for i in range(len(c)-1) :
    result += cost[i] * l[i]
    
print(result)
        

    