from collections import deque

n = int(input()) # 전체 사람의 수
a, b = map(int, input().split()) # 계산해야 하는 번호
r = int(input()) # 관계 수

human = [[]*(n+1) for _ in range(n+1)]
visited = [False] * (n+1)
graph = [0] * (n+1)

for _ in range(r) :
    m, n = map(int, input().split())
    human[m].append(n)
    human[n].append(m)
    
def bfs(x) :
    q = deque()
    q.append(x)
    visited[x] = True
    
    while(q) :
        x1 = q.popleft()
        
        for i in human[x1] :
            if visited[i] == True : continue
            
            q.append(i)
            visited[i] = True
            graph[i] = graph[x1] + 1
            
            if i == b :
                return True
            
    return False

if bfs(a) == True : print(graph[b])
else : print(-1)
            
            
    
    
