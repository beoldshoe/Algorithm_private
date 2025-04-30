def bfs(x, y) :
    q = deque()
    q.append((x,y))
    visited[x][y] = True

    x = [-1, -1, 0, 1, 1, 1, 0, -1]
    y = [0, 1, 1, 1, 0, -1, -1, -1]

    while(q) :
        x1, y1 = q.popleft()
        for i in range(8) :
            dx = x[i] + x1
            dy = y[i] + y1

            if dx < 0 or dy < 0 or dx >=h or dy >= w :
                continue

            if visited[dx][dy] == True : continue
            if graph[dx][dy] == 1 :
                visited[dx][dy] = True
                q.append((dx, dy))

from collections import deque

while(1) :
    w, h = map(int,input().split())
    if w == 0 and h == 0 : break
    graph = []
    visited = [[False] * w for _ in range(h)]
    # print(visited)
    # if w == 1 :
    #     for _ in range(h) :
    #         l = list(input())
    #         graph.append(l)
    # else :
    #     for _ in range(h) :
    for _ in range(h) :
        l = list(map(int, input().split()))
        graph.append(l)
    cnt = 0
    for i in range(h) :
        for j in range(w) :
            if visited[i][j] == True : continue
            if graph[i][j] == 1 :
                bfs(i, j)
                cnt += 1

    print(cnt)


            
