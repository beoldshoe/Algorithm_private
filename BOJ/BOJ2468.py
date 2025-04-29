from collections import deque
import copy

# 잠겼으면 0, 안 잠겼으면 1
def change_graph(num) :
    for i in range(N) :
        for j in range(N) :
            if change[i][j] > num : # 안 잠겼으면 
                change[i][j] = 0
            else : # 잠겼으면
                change[i][j] = 1

def bfs(x, y) :
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    nx = [0, 0, 1, -1]
    ny = [1, -1, 0, 0]
    
    while(q) :
        x1, y1 = q.popleft() 
        for c in range(4) :
            dx = nx[c] + x1
            dy = ny[c] + y1
            
            if dx < 0 or dy < 0 or dx >= N or dy >= N : continue
            if visited[dx][dy] == True : continue
                
            if change[dx][dy] == 0 :
                q.append((dx, dy))
                visited[dx][dy] = True
                
N = int(input())
graph = []

mn = 200
mx = -1

for _ in range(N) :
    i = list(map(int, input().split()))
    
    if mn > min(i) :
        mn = min(i)
    
    if mx < max(i) :
        mx = max(i)

    graph.append(i)

result = []   
for i in range(0, mx) :
    cnt = 0
    change = []
    change = copy.deepcopy(graph)
    change_graph(i)
    visited = [[False] * (N+1) for _ in range(N+1)]
    for j in range(N) :
        for k in range(N) :
            if change[j][k] == 0 : 
                if visited[j][k] == True : continue
                bfs(j, k)
                cnt += 1
    result.append(cnt)
if len(result) == 0 :
    print(0)
else :
    print(max(result))