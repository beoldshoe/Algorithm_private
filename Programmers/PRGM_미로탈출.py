from collections import deque

def solution(maps):
    sx = 0
    sy = 0
    lx = 0
    ly = 0

    for i in range(len(maps)) :
        for j in range(len(maps[i])) :
            if maps[i][j] == "S" :
                sx = i
                sy = j
            if maps[i][j] == "L" :
                lx = i
                ly = j

    def findl_bfs(x, y) :
        q = deque()
        idx = 0
        q.append((x, y, idx))
        nx = [-1, 1, 0, 0]
        ny = [0, 0, 1, -1]
        visited = [[False] * len(maps[0]) for _ in range(len(maps))]
        visited[x][y] = True
        while q :
            cx, cy, cidx = q.popleft()
            for i in range(4) :
                dx = cx + nx[i]
                dy = cy + ny[i]
                
                if dx < 0 or dy < 0 or dx >= len(maps) or dy >= len(maps[0]) : continue
                if maps[dx][dy] == 'X' : continue
                if visited[dx][dy] : continue

                if dx == lx and dy == ly :
                    return cidx + 1
                
                if maps[dx][dy] in ('O', 'E'):
                    q.append((dx, dy, cidx+1))
                    visited[dx][dy] = True                    
        return -1
    
    def finde_bfs(x, y) :
        q = deque()
        idx = 0
        q.append((x, y, idx))
        visited = [[False] * len(maps[0]) for _ in range(len(maps))]
        visited[x][y] = True
        nx = [-1, 1, 0, 0]
        ny = [0, 0, 1, -1]
        while q :
            cx, cy, cidx = q.popleft()
            for i in range(4) :
                dx = cx + nx[i]
                dy = cy + ny[i]
                
                if dx < 0 or dy < 0 or dx >= len(maps) or dy >= len(maps[0]) : continue
                if maps[dx][dy] == 'X' : continue
                if visited[dx][dy] : continue
                
                if maps[dx][dy] == 'E' :
                    return cidx + 1
                
                if maps[dx][dy] in ('O', 'S'):
                    q.append((dx, dy, cidx+1))
                    visited[dx][dy] = True  
                    
        return -1

    f = findl_bfs(sx, sy)
    if f == -1 : return -1
    e = finde_bfs(lx, ly)
    if e == -1 : return -1
    
    return f + e