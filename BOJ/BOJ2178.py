# N, M = map(int,input().split())
# list = []
# for _ in range(N) :
#     maze = input()
#     list.append(maze)
# cnt = 0
# def check(i, j, cnt) :
#     if list[i][j] == '1' :
#         cnt += 1
#     else : return
    
#     if i == 0 :
#         check(i+1, j, cnt)
#         if j == 0 :
#             check(i, j+1, cnt)
#         elif j == M-1 :
#             check(i, j-1, cnt)
#         else :
#            check(i, j-1, cnt)
#            check(i, j+1, cnt) 
#     elif i == N -1 :
#         check(i-1, j, cnt)
#         if j == 0 :
#             check(i, j+1, cnt)
#         elif j == M-1 :
#             if list[i][j] == '1' :
#                 return cnt
#         else :
#             check(i, j+1, cnt)
#             check(i, j-1, cnt)
#     else :
#        check(i-1, j, cnt)
#        check(i+1, j, cnt)
#        if j == 0  :
#           check(i, j+1, cnt)
#        elif j == M-1 :
#            check(i, j-1, cnt)
#        else :
#         check(i, j+1, cnt)
#         check(i, j-1, cnt)
        
        
# print(check(0, 0, 0))

from collections import deque

N, M = map(int, input().split())

graph = []

for _ in range(N):
    graph.append(list(map(int, input())))

def BFS(x, y):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=N or ny<0 or ny>=M:
                continue
            if graph[nx][ny]==0:
                continue
            if graph[nx][ny]==1:
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx,ny))

    return graph[N-1][M-1]

print(BFS(0,0))