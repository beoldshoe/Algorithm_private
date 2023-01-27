n = input()

moving_way = [[-2,-1],[-2,1], [2,-1],[2,1],[-1,-2],[-1,2],[1,-2],[1,2]]

'''for i, j in range(len(moving_way)) :
    a = ord(n[i])-96+moving_way[i]
    b = ord(n[j])-48+moving_way[j]
    result.append(a, b)'''
a = ord(n[0])-96
b = ord(n[1])-48

result = list()
'''print(result)
print(moving_way[0][0])
print(moving_way[0][1])'''

'''result.append([a + moving_way[0][0], b + moving_way[0][1]])
print(result)'''

for i in range(len(moving_way)):
        result.append([a+moving_way[i][0], b+moving_way[i][1]])

'''print(result)'''

count = 0

for i in range(len(moving_way)):
    if result[i][0] >=1 and result[i][0]<=8:
        if result[i][1] >=1 and result[i][1] <=8 :
            count = count + 1
        else :
            count = count
    else :
        count = count
    
print(count)
        