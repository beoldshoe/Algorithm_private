N = int(input())
num_list = []
for _ in range(N) :
    num = int(input())
    num_list.append(num)

num_list = sorted(num_list, reverse=True)
for x in num_list :
    print(x)