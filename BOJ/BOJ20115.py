N = int(input())

l = list(map(int, input().split()))

l.sort()

result = l[-1]

for i in range(len(l)-1) :
    result += l[i]/2

print(result)

