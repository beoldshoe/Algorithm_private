# from collections import deque

# N = int(input())
# l = []
# visited = [False] * (N+1)

# for _ in range(N) :
#     a = list(input())
#     l.append(a)

# def bfs(i, visited, cnt) :
#     q = deque()
#     q.append(i)

#     while(q) :
#         ni = q.popleft()

#         if visited[ni] == True :
#             continue
#         for i in l[ni] :
#             if i == 'Y' :
#                 if visited[i] != False :
#                     visited[i] = True
#                     cnt += 1
#                     q.append(i)

#     return cnt
# result = []
# for i in range(N) :
#     if visited[i] == False :
#         r = bfs(i, visited, 0)
#         result.append(r)

# print(max(result))


# import sys
# input = sys.stdin.readline

# A가 B와 2-친구가 되기위한 조건
# 1. A와 B가 친구사이이어야 함
# 2. A와 친구이고, B와 친구인 C가 존재해야된다.

# # 사람의 수
# n = int(input().strip())

# # 친구관계 입력받기
# friends = []
# for _ in range(n):
#     friends.append(list(input().strip()))
    
# INF = int(1e9)

# # 최단거리 테이블 생성(INF는 친구관계가 아닌 경우에 저장된다.)
# dist = [[INF] * n for _ in range(n)]

# for i in range(n):
#     for k in range(n):
#         if friends[i][k] == 'Y':
#             dist[i][k] = 1
#         if i == k:
#             dist[i][k] = 0

# # 플로이드 워셜 알고리즘을 이용하여 친구관계 사이의 거리를 계산하여 최단거리 테이블을 갱신한다.
# def floid():
#     for i in range(n):
#         for k in range(n):
#             for h in range(n):
#                 if i == k or i == h or k == h:
#                     continue
#                 else:
#                     dist[k][h] = min(dist[k][h], dist[k][i] + dist[i][h])

# floid()
# # for i in dist:
# #     print(i)

# # i와 k사이의 거리가 2 이하인 경우는 2-친구의 조건을 만족하기 때문에 갯수를 센다
# result = 0
# for i in range(n):
#     cnt = 0
#     for k in range(n):
#         if i == k:
#             continue
#         if dist[i][k] <= 2:
#             cnt += 1
#     result = max(result, cnt)
# print(result)

N = int(input())
l = []
for _ in range(N) :
    a = list(input())
    l.append(a)


INF = int(1e9)
graph = [[INF] * N for _ in range(N)]

for i in range(N) :
    for j in range(N) :
        if l[i][j] == 'Y' :
            graph[i][j] = 1
        if i == j : 
            graph[i][j] = 0

def floid() :
    for k in range(N) :
        for i in range(N) :
            for j in range(N) :
                if k == i or i == j or k ==j :
                    continue
                else :
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
floid()
result = 0
for i in range(N) :
    cnt = 0 
    for j in range(N) :
        if i == j : continue
        if graph[i][j] <= 2 :
            cnt += 1
    result = max(result, cnt)
print(result)

