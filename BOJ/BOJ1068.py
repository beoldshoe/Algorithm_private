from collections import deque

def bfs(x, visited) :
    q = deque()
    q.append(x)
    visited[x] = True
    cnt = 0
    if len(graph[x]) == 0 :
        cnt += 1
    while(q) :
        x1 = q.popleft()
        for i in graph[x1] :
            if visited[i] == True : continue
            if len(graph[i]) == 0 :
                cnt += 1
            q.append(i)
            visited[i] = True  
    return cnt

N = int(input())

tree = list(map(int, input().split()))

graph = [[] * N for _ in range(N)]
start = 0
delete = int(input())
for i in range(len(tree)) :
    if tree[i] == -1 :
        start = i
    else :
        if i != delete :
            graph[tree[i]].append(i)
if start == delete :
    print(0)
    exit(0)
visited = [False] * N

result = bfs(start, visited)
print(result)

# 참고 블로그
# https://velog.io/@ice-prince/%EB%B0%B1%EC%A4%80-1068-%ED%8A%B8%EB%A6%AC-Python