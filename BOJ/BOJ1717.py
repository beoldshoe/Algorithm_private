a, b = map(int, input().split())

ids = []
size = []
for idx in range(a+1) :
    ids.append(idx)
    size.append(1)

def root(i) :
    while i != ids[i] :
        i = ids[i]
    return i

def connected(p, q) :
    return root(p) == root(q)

def union(p,q) :
    id1, id2 = root(p), root(q)
    if id1 == id2 :
        return
    if size[id1] <= size[id2] :
        ids[id1] = id2
        size[id2] += size[id1]
    else :
        ids[id2] = id1
        size[id1] += size[id2]
        
for i in range(b) :
    c, d, e = map(int, input().split())
    if c == 0 :
        union(d,e)
    else :
        if connected(d,e) == True:
            print('YES')
        else :
            print('NO')
    # print(ids) -> 디버깅용