from collections import deque

# def solution(places):
    
#     def bfs(si, sj, ei, ej, idx) :
#         q = deque()
#         visited = [[False] * 5 for _ in range(5)]
#         cnt = 0
#         q.append((si, sj, cnt))
#         visited[si][sj] = True
#         dx = [0,0,1,-1]
#         dy = [1,-1,0,0]
        
#         while(q) :
#             ci, cj, ccnt = q.popleft() 
#             for i in range(4) :
#                 nx = ci + dx[i]
#                 ny = cj + dy[i]
                
#                 if nx < 0 or ny < 0 or nx >=5 or ny >= 5 : continue
#                 if visited[nx][ny] == True : continue
#                 if places[idx][nx][ny] == "X" : continue
#                 if nx == ei and ny == ej :
#                     return ccnt
                
#                 if places[idx][nx][ny] == "O" or places[idx][nx][ny] == "P" :
#                     visited[nx][ny] = True
#                     q.append((nx, ny, ccnt+1))
                    
#         return ccnt
    
#     result = []   
#     for i in range(5) :
#         p_list = []
#         for j in range(5) :
#             for k in range(5) :
#                 if places[i][j][k] == 'P' :
#                     p_list.append((j,k))
#         check = 0
#         if len(p_list) == 0 :
#             result.append(1)
#             continue
#         for r in range(len(p_list)-1) :
#             for v in range(r+1, len(p_list)) :
#                 si, sj = p_list[r]
#                 ei, ej = p_list[v]
#                 if abs(si-ei) + abs(sj-ej) <=2 : 
#                     if bfs(si, sj, ei, ej, i) == 1 or bfs(si, sj, ei, ej, i) == 2 :
#                         result.append(0)
#                         check = 1
#                         break
#             if check == 1 :
#                 break
#         if check == 0 :
#             result.append(1)
                
#     return result

def solution(places):
    result = []
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    nx,ny,px,py = 0,0,0,0
    def bfs(i):
        for j in range(5):
                for z in range(5):
                    if places[i][j][z] == 'P': # P를 탐색
                        for p in range(4):
                            nx = j + dx[p]
                            ny = z + dy[p]
                            if nx < 0 or ny < 0 or nx >= 5 or ny >= 5:
                                continue # 크기를 벗어나는 경우 패스
                            if places[i][nx][ny] == 'O':  # 0을 발견하는 경우 주위 탐색
                                for p in range(4):
                                    px = nx + dx[p]
                                    py = ny + dy[p]
                                    if px == j and py == z:
                                        continue
                                    if px < 0 or py < 0 or px >= 5 or py >= 5:
                                        continue
                                    if places[i][px][py] == 'P': 
                                        return 0
                            else:
                                if places[i][nx][ny] == 'P': # 바로 P발견인 경우 0
                                    return 0
        return 1 # P가 없거나, 모두 끝났으나, 문제가 없을경우
        
    for i in range(len(places)): # 주어진 케이스 만큼 돌리기
        result.append(bfs(i))
    return result
                
                