N = int(input())
costs = []
for _ in range(N) :
    cost = int(input())
    costs.append(cost)
    
costs.sort(reverse=True)
result = 0
for i in range(len(costs)) :
    if i % 3 != 2 :
        result += costs[i]
        
print(result)