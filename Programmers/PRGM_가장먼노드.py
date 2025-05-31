from collections import deque

def solution(n, edge):
    def bfs(i, visited) :
        q = deque()
        idx = 0
        q.append((i, idx))
        visited[i] = True 
        while(q) :
            x, idx1 = q.popleft()
            for j in graph[x] :
                if visited[j] == True : continue
                if idx1 in result.keys() :
                    result[idx1] += 1
                else :
                    result[idx1] = 1
                q.append((j, idx1 + 1))
                visited[j] = True


    graph = [[]*(n+1) for _ in range(n+1)]
    visited = [False] * (n+1)
    result = {}
    for i in edge :
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])

    bfs(1, visited)

    m = max(result.keys())
    return result[m]