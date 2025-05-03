from collections import deque

def bfs(x, y, visited) :
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    cnt = 1
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    while(q) :
        x1, y1 = q.popleft()
        for i in range(4) :
            nx = dx[i] + x1
            ny = dy[i] + y1

            if nx < 0 or ny < 0 or nx >= M or ny >= N :
                continue
            
            if visited[nx][ny] == True : continue
            if graph[nx][ny] == 0 : continue
            cnt += 1
            q.append((nx, ny))
            visited[nx][ny] = True
            
    return cnt

M, N, K = map(int, input().split())

graph = [[1]* N for _ in range(M)]
visited = [[False]* N for _ in range(M)] 
for _ in range(K) :
    x1, y1, x2, y2 = map(int, input().split())
    
    for i in range(y1, y2) :
        for j in range(x1, x2) :
            if graph[i][j] == 0 : continue
            graph[i][j] = 0
result = []
for i in range(M) :
    for j in range(N) :
        if visited[i][j] == True : continue
        if graph[i][j] == 0 : continue
        result.append(bfs(i, j, visited))
        
result.sort()
print(len(result))
print(*result)