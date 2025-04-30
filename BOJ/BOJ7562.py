from collections import deque

def bfs(startx, starty, endx, endy, visited) :
        q = deque()
        q.append((startx, starty))
        visited[startx][starty] = True

        while(q) :
            x = [-2, -1, 1, 2, 2, 1, -1, -2]
            y = [1, 2, 2, 1, -1, -2, -2, -1]
            x1, y1 = q.popleft()

            for i in range(8) :
                dx = x[i] + x1
                dy = y[i] + y1
                if dx < 0 or dy < 0 or dx > l-1 or dy> l-1 : continue
                if visited[dx][dy] == True : continue
                graph[dx][dy] = graph[x1][y1] + 1
                visited[dx][dy] = True
                if dx == endx and dy == endy :
                    return
                q.append((dx, dy))
                

T = int(input())

for _ in range(T) :
    l = int(input())
    graph = [[0] * l for _ in range(l)]
    visited = [[False] * l for _ in range(l)]
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    if sx == ex and sy == ey :
        print(0)
    else :
        bfs(sx, sy, ex, ey, visited)
        print(graph[ex][ey])