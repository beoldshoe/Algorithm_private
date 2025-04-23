from collections import deque

def BFS(i1, j1) :
    queue = deque()
    queue.append((i1, j1))
    graph[i1][j1] = 0

    x = [0, 0, -1, 1]
    y = [1, -1, 0, 0]
    while queue :
        x1, y1 = queue.popleft()

        for i in range(4) :
            nx = x1 + x[i]
            ny = y1 + y[i]

            if nx < 0 or ny < 0 or nx>=M or ny >= N :
                continue
            if graph[nx][ny] == 1 :
                queue.append((nx, ny))
                graph[nx][ny] = 0

T = int(input())

for _ in range(T) :
    M, N, K = map(int, input().split())
    graph = [[0] * N for _ in range(M)]

    for _ in range(K) :
        i, j = map(int,input().split())
        graph[i][j] = 1

    cnt = 0
    for i in range(M) :
        for j in range(N) :
            if graph[i][j] == 1:
                BFS(i, j)
                cnt += 1
    print(cnt)

# 참고 블로그
# https://velog.io/@hyooo1022/%EB%B0%B1%EC%A4%80-1012%EB%B2%88-%EC%9C%A0%EA%B8%B0%EB%86%8D-%EB%B0%B0%EC%B6%94



        
