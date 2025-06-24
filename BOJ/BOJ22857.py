n, k = map(int, input().split())
arr = list(map(int, input().split()))
 
# 행 : arr 인덱스
# 열 : 원소 삭제 횟수
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
for i in range(1, n + 1):
    for j in range(k + 1):
        if arr[i-1] % 2 == 1: # 홀수이면
            if j > 0:
                dp[i][j] = dp[i-1][j-1] 
        else:               # 짝수이면
            dp[i][j] = dp[i-1][j] + 1
            
max_length = 0
for r in dp:
    for c in r:
        max_length = max(max_length, c)
print(max_length)

# 참고 블로그 
# https://zero0205.tistory.com/276