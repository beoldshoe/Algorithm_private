N, M = map(int, input().split())
memo = {}
for _ in range(N) :
    add, pw = map(str, input().split())
    memo[add] = pw

for _ in range(M) :
    search_add = str(input())
    print(memo[search_add])