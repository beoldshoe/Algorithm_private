from math import gcd

a, b = map(int, input().split())

print(gcd(a, b))
print(int(a * b / gcd(a,b)))