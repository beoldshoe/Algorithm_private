from collections import deque

N = int(input())

graph = list(map(int, input().split()))
visited = [False] * (N+1)
count = [0] * (N+1)

def bfs(x) :
    q = deque()
    q.append(x) # 인덱스 저장
    visited[x] = True
    if x == N -1 :
        return True
    
    while(q) :
        a = q.popleft() # 인덱스 불러오기
        x1= graph[a] # 숫자 불러오기
        for i in range(1, x1+1) :
            dx = a + i # 지금 인덱스에서 다음 갈 인덱스 정하기
            
            if dx >= N : continue
            if visited[dx] == True : continue
            
            q.append(dx)
            visited[dx] = True
            count[dx] = count[a] + 1
            if dx == N-1 : 
                return True
            
    return False

if bfs(0) == True :
    print(count[N-1])
else :
    print(-1)  