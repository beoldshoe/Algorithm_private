from collections import deque

n, m = map(int, input().split())

arr = [list(input()) for _ in range(n)]
visited = [[0 for j in range(m)] for _ in range(n)]

count = 0

def make_icecream(arr, visited, a, b) :
    queuefori = deque([a])
    queueforj = deque([b])
    global n
    global m
    global count
    while queuefori and queueforj :
        a = queuefori.popleft()
        b = queueforj.popleft()
        if arr[a][b] == '0' :
            visited[a][b] = 1
            if b+1 < m:
                if arr[a][b+1] == '0' :
                    if visited[a][b+1] == 0 :
                        queuefori.append(a)
                        queueforj.append(b+1)
                        visited[a][b+1] = 1
            if a+1 < n :            
                if arr[a+1][b] == '0' :
                    if visited[a+1][b] == 0 :
                        queuefori.append(a+1)
                        queueforj.append(b)
                        visited[a+1][b] = 1



for i in range(n):
    for j in range(m):
        if arr[i][j] == '0' and visited[i][j] == 0 :
            make_icecream(arr, visited, i, j)
            count = count + 1
            
print(count)
