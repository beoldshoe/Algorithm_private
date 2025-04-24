from collections import deque

N, K = map(int, input().split())
MAX = 10 ** 5
graph = [0] * (MAX + 1)


def BFS(i) :
    queue = deque()
    queue.append(i)
    
    while(queue) :
        x = queue.popleft()
        if x == K :
            return graph[K]
        for i in (x+1, x-1, x*2) :
            if 0<= i<=MAX and graph[i] == 0:
                graph[i] = graph[x] + 1
                queue.append(i)
        
print(BFS(N))

# 참고 블로그 
# https://velog.io/@nimoh/Python-%EB%B0%B1%EC%A4%80-1697-%EC%88%A8%EB%B0%94%EA%BC%AD%EC%A7%88