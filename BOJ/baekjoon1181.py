N = int(input())
list = []

for i in range(N):
    list.append(input())

list.sort()
list.sort(key=len)

now = "0"

for i in list:
    if now == i :
         continue
    else :
        now = i
        print(i)