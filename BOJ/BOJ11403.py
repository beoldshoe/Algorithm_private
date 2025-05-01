from collections import deque

def bfs(x, y, visited) :
    q = deque()
    q.append(x)
    
    while(q) :
        x1 = q.popleft()
        if len(graph[x1]) == 0 : continue
        for i in graph[x1] :
            if i == y :
                return True
            if visited[x1][i] == True : continue
            visited[x1][i] = True
            q.append(i)
            
    return False
            

N = int(input())
l = []
for _ in range(N) :
    l.append(list(map(int, input().split())))
    
graph = [[]*N for _ in range(N)]
for i in range(N) :
    for j in range(N) :
        if l[i][j] == 1 :
            graph[i].append(j)
            
result = [[0] * N for _ in range(N)]
for i in range(N) :
    for j in range(N) :
        visited = [[False] * N for _ in range(N)]
        r = bfs(i, j, visited)
        if r == True :
            result[i][j] = 1
            
for i in range(N) :
    print(*result[i])