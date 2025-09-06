from collections import deque
import sys
input = sys.stdin.readline

N, M , fuel = map(int, input().split())
graph = []
for _ in range(N) :
    a = map(int,input().split())
    graph.append(list(a))

car_start_x, car_start_y = map(int,input().split())
car_start_x = car_start_x-1
car_start_y = car_start_y-1
person_start= []
person_end= []
for _ in range(M) :
    person_start_x, person_start_y, person_end_x, person_end_y = map(int,input().split())
    person_start.append((person_start_x-1, person_start_y-1))
    person_end.append((person_end_x-1, person_end_y-1))


def dfs(sx, sy, ex, ey, visited) :
    q = deque()
    cnt = 0
    q.append((sx,sy, cnt))
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    visited[sx][sy] = True
    while(q) :
        nx, ny, ncnt = q.popleft()
        for i in range(4) :
            gx = nx + dx[i]
            gy = ny + dy[i]   
            if gx <0 or gy < 0 or gx >= N or gy >= N :
                continue
            if graph[gx][gy] == 1 : continue
            if visited[gx][gy] == True : continue
            if gx == ex and gy == ey :
                return ncnt+1
            q.append((gx, gy, ncnt+1))
            visited[gx][gy] = True
    return -1

def bfs_all(sx, sy):
    dist = [[-1]*N for _ in range(N)]
    q = deque()
    dist[sx][sy] = 0
    q.append((sx, sy))
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if graph[nx][ny] == 1 or dist[nx][ny] != -1:
                continue
            dist[nx][ny] = dist[x][y] + 1
            q.append((nx, ny))
    return dist


tx, ty = car_start_x, car_start_y

for _ in range(M):

    dist_from_taxi = bfs_all(tx, ty)

    candidates = []
    for i in range(M):
        sx, sy = person_start[i]
        if sx == -1:  
            continue
        d = dist_from_taxi[sx][sy]
        if d != -1:
            candidates.append((d, sx, sy, i))

    if not candidates:  
        print(-1)
        sys.exit(0)

    candidates.sort() 
    d1, psx, psy, idx = candidates[0]

    if d1 > fuel:
        print(-1)
        sys.exit(0)

    fuel -= d1
    tx, ty = psx, psy

    visited = [[False] * N for _ in range(N)]
    d2 = dfs(tx, ty, person_end[idx][0], person_end[idx][1], visited)
    if d2 == -1 or d2 > fuel:
        print(-1)
        sys.exit(0)

    fuel = fuel - d2 + 2*d2  
    tx, ty = person_end[idx]

    person_start[idx] = (-1, -1)

print(fuel)