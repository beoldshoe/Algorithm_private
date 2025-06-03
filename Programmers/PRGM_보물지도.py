from collections import deque
def solution(n, m, hole):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    graph = [[0] * m for _ in range(n)]
    for a,b in hole:
        graph[a-1][b-1] = 1
    
    queue = deque() 
    visited = [[[False] * 2 for _ in range(m)] for _ in range(n)] 
    visited[0][0][False] = True 
    queue.append((0,0,False))
    L = 0
    
    while queue:
        
        for _ in range(len(queue)):
            x,y,used = queue.popleft()
                  
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny][used] and graph[nx][ny] == 0:
                    if (nx,ny) == (n-1,m-1):
                        return L + 1
                    visited[nx][ny][used] = True
                    queue.append((nx,ny,used))
                    
                if not used: 
                    nx += dx[i]
                    ny += dy[i]
                    if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny][used] and graph[nx][ny] == 0:
                        if (nx,ny) == (n-1,m-1):
                            return L + 1
                        visited[nx][ny][True] = True
                        queue.append((nx,ny,True))
        L += 1    
    return -1