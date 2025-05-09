from collections import deque

def bfs(x, y) :
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    cnt = 0
    nx = [1, 0 , -1, 0]
    ny = [0, 1, 0, -1]

    while(q) :
        x1, y1 = q.popleft()
        for i in range(4) :
            dx = x1 + nx[i]
            dy = y1 + ny[i]

            if dx < 0 or dy < 0 or dx >= N or dy >= M :
                continue

            if visited[dx][dy] == True : continue
            if graph[dx][dy] == 1 : continue

            visited[dx][dy] = True
            q.append((dx, dy))

            if graph[dx][dy] == 2:
                cnt += 1

    return cnt

N, M = map(int, input().split())
graph = []
doyeon_x = 0
doyeon_y = 0

visited = [[False] * (M+1) for _ in range(N+1)]
for _ in range(N) :
    l = list(input())
    graph.append(l)

for i in range(N) :
    for j in range(M) :
        if graph[i][j] == 'O' :
            graph[i][j] = 0
        elif graph[i][j] == 'I' :
            doyeon_x = i
            doyeon_y = j
            graph[i][j] = 0
        elif graph[i][j] == 'X' :
            graph[i][j] = 1
        else :
            graph[i][j] = 2

r = bfs(doyeon_x, doyeon_y)

if r == 0 :
    print('TT')
else : print(r)

            
