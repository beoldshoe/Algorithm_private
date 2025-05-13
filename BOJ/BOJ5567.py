from collections import deque

n = int(input())
m = int(input())
graph = [[]*(n+1) for _ in range(n+1)]
visited = [False]*(n+1)
count = [0] * (n+1)
for _ in range(m) :
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def bfs(x) :
    q = deque()
    q.append(x)
    visited[x] = True
    
    while(q) :
        x1= q.popleft()
        for i in graph[x1] :
            if visited[i] == True : continue
            q.append(i)
            visited[i] = True
            count[i] = count[x1] + 1
            
bfs(1)
cnt = 0
for i in count :
    if i != 0 :
        if i <= 2 :
            cnt += 1
        
print(cnt)
            
            