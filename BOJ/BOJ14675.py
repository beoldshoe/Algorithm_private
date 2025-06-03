import sys

N = int(input())
graph = [[] * (N+1) for _ in range(N+1)]
for i in range(N-1) :
    a, b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

q = int(input())
for _ in range(q) :
    t, k = map(int,sys.stdin.readline().split())
    if t == 1 :
        if (len(graph[k]) < 2):
            print("no")
        else:
            print("yes")
    else :
        print('yes')