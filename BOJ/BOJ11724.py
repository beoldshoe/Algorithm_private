# N, M = map(int, input().split())

# dic = {}
# id = 1
# for _ in range(M) :
#     u, v = map(int, input().split())
#     if u in dic.keys() :
#         if v in dic.keys() :

#     else :
#         dic[u] = id
#         dic[v] = id
#         id += 1

# print(len(set(dic.values())))

from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# bfs 함수
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

n, m = map(int, input().split()) 
graph = [[] for _ in range(n+1)]
for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

count = 0
visited = [False] * (n+1)
for i in range(1, n+1):
    if not visited[i]:
        bfs(graph, i, visited)
        count += 1

print(count)

