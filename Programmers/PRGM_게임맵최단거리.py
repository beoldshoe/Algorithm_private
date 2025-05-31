from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[False] * m for _ in range(n)]
    def bfs(x, y, visited) :
        q = deque()
        cnt = 0
        q.append((x,y,cnt))
        visited[x][y] = True
        
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        
        while(q) :
            x1, y1, dist = q.popleft()
            if x1 == m-1 and y1 == n-1 : 
                return dist+1
            for i in range(4) :
                nx = x1 + dx[i]
                ny = y1 + dy[i]
                if nx >= m or ny >= n or nx < 0 or ny < 0 : continue
                if visited[ny][nx] == True : continue
                if maps[ny][nx] == 0 : continue
                q.append((nx, ny, dist + 1))
                visited[ny][nx] = True
                
        return -1
    if maps[0][0] == 0 : 
        return - 1
    else :
        return bfs(0, 0, visited)