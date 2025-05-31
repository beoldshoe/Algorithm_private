from collections import deque

def solution(city):
    m = len(city)
    n = len(city[0])
    visited = [[False] * n for _ in range(m)]
    def bfs(x, y, visited) :
        q = deque()
        cnt = 0
        q.append((x, y, cnt))
        visited[x][y] = True
        dx = [1, 1, 0, -1, -1, -1, 0, 1]
        dy = [0, -1, -1, -1, 0, 1, 1, 1]

        while(q) :
            x1, y1, tmp = q.popleft()
            if x1 == n-1 and y1 == m -1 : 
                return tmp + 1
            for i in range(8) :
                nx = x1 + dx[i]
                ny = y1 + dy[i]

                if nx >= n or ny >= m or nx < 0 or ny < 0 : continue
                if visited[ny][nx] == True : continue
                if city[ny][nx] == 1 : continue
                visited[ny][nx] = True
                q.append((nx, ny, tmp+1))
                
        return -1
    if city[0][0] == 1 :
        return -1
    else : result = bfs(0, 0, visited)
    return result