from math import gcd

n = int(input())

for _ in range(n) :
    a, b = map(int, input().split())
    print(a* b // gcd(a,b))