import heapq

n = int(input())
table = []

for _ in range(n) :
    d, c = map(int, input().split())
    table.append((d,c))
table.sort()

stack = []

for i in table :
    heapq.heappush(stack, i[1])
    if i[0] < len(stack) :
        heapq.heappop(stack)

print(sum(stack))