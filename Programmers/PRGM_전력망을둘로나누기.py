# from collections import deque

# def solution(n, wires):
    
#     def bfs_depth(x, visited) :
#         q = deque()
#         depth = 0
#         q.append((x, depth))
#         visited[x] = True
        
#         while(q) :
#             x1, depth1 = q.popleft()
#             for i in graph[x1] :
#                 if visited[i] == True : continue
#                 q.append((i, depth1+1))
#                 visited[i] = True
                
#         return depth1
    
#     def bfs_count(x, visited) :
#         q = deque()
#         count = 0
#         q.append(x)
#         visited[x] = True
        
#         while(q) :
#             x1 = q.popleft()
#             for i in graph[x1] :
#                 if visited[i] == True : continue
#                 q.append(i)
#                 count += 1
#                 visited[i] = True
                
#         return count

#     graph = [[] for _ in range(n+1)]
    
#     for w in wires :
#         graph[w[0]].append(w[1])
#         graph[w[1]].append(w[0])
        
#     dep = []
#     for i in range(1, n+1) :
#         visited = [False] * (n+1)
#         d = bfs_depth(i, visited)
#         dep.append((d, i))
        
#     dep.sort(reverse = True)
#     idx1 = dep.pop()[1]
#     idx2 = dep.pop()[1]
    
#     visited1 = [False] * (n+1)
#     visited1[idx2] = True
#     visited2 = [False] * (n+1)
#     visited2[idx1] = True
#     a = bfs_count(idx1, visited1)
#     b = bfs_count(idx2, visited2)
    
#     return abs(a-b)
        
from collections import deque

def bfs(start, visited, graph):
    q = deque([start])
    visited[start] = True
    count = 1
    
    while q:
        node = q.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                q.append(neighbor)
                count += 1
    return count

def solution(n, wires):
    answer = n 

    for i in range(len(wires)):
        graph = [[] for _ in range(n+1)]
        for j in range(len(wires)):
            if i == j:
                continue
            a, b = wires[j]
            graph[a].append(b)
            graph[b].append(a)

        visited = [False] * (n+1)
        count = bfs(1, visited, graph) 
        answer = min(answer, abs(n - count - count))  

    return answer