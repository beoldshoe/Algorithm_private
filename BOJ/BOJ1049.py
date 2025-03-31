N, M = map(int, input().split())
all_cost = []
one_cost = []
for _ in range(M) :
    all, one = map(int, input().split())
    all_cost.append(all)
    one_cost.append(one)

all_cost.sort()
one_cost.sort()
result = 0 

a = N // 6
b = N % 6
if all_cost[0] > one_cost[0] * 6 :
    result += a * (one_cost[0] * 6)
else :
    result += a * all_cost[0]

if all_cost[0] > one_cost[0] * b :
    result += one_cost[0] * b
else :
    result += all_cost[0]

print(result)