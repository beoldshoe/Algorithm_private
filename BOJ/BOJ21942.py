from collections import defaultdict
import sys
input = sys.stdin.readline
N, L, F = map(str, input().rstrip().split())
N, F = int(N), int(F)
days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
x = L.split('/')
y = x[1].split(':')
L = int(y[1]) + int(y[0]) * 60 + int(x[0]) * 60 * 24

borrow = {}
ans = defaultdict(int)
for _ in range(N) :
    info = input().rstrip().split()
    date = list(map(int, info[0].split('-')))
    time = list(map(int, info[1].split(':')))
    object = info[2]
    name = info[3].strip()

    t = time[1] + time[0]*60
    t += (date[2]-1) * 24 * 60
    t += 24 * 60 * sum(days[:date[1]])

    if (name, object) not in borrow or borrow[(name, object)] == -1 :
        borrow[(name, object)] = t
    else :
        if borrow[(name, object)] + L < t :
            ans[name] += (t-(borrow[(name, object)] + L)) * F
        borrow[(name, object)] = -1

if ans :
    ans = list(ans.items())
    ans.sort()
    for a in ans :
        print(a[0], a[1])
else :
    print(-1)

# 참고 블로그
# https://velog.io/@ya_ong/%EB%B0%B1%EC%A4%80%ED%8C%8C%EC%9D%B4%EC%8D%AC-21942-%EB%B6%80%ED%92%88-%EB%8C%80%EC%97%AC%EC%9E%A5