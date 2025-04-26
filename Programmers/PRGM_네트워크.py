from collections import deque

def solution(n, computers):
    
    def bfs(i,visited) :
        q = deque()
        q.append(i)

        visited[i] = True
        
        while(q) :
            index = q.popleft()
            for ni in range(len(computers[index])) :

                if visited[ni] == True :
                    continue
                    
                if ni != index :
                    if computers[index][ni] == 1 :
                        q.append(ni)
                        visited[ni] = True
    
    visited = [False] * (n+1)
    cnt = 0
    for i in range(n) :
        if visited[i] == False :
            bfs(i, visited)
            cnt += 1
            
    return cnt

