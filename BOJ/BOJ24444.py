from collections import deque
import sys

N, M, R = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
count = [0] * (N+1)

for _ in range(M) :
    u, v = map(int, sys.stdin.readline().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(N+1):
    graph[i].sort()

def bfs(x) :
    q = deque()
    q.append(x)
    cnt = 1
    visited[x] = True
    count[x] = cnt
    cnt += 1

    while(q) :
        x1 = q.popleft()
        if len(graph[x1]) == 0 : continue
        for i in graph[x1] :
            if visited[i] == True : continue
            visited[i] = True
            count[i] = cnt
            cnt += 1
            q.append(i)

bfs(R)

for i in range(1, N+1) :
    print(count[i])