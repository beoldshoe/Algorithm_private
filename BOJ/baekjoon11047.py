N, K = map(int, input().split())
coin = list()
for i in range(N):
    coin.append(int(input()))

count = 0
for j in reversed(range(N)) :
    count += K//coin[j]
    K = K % coin[j]
    

print(count)
    