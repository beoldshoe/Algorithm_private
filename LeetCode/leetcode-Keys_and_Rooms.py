# from collections import deque

# class Solution:
#     def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
#         def bfs(i, visited) :
#             q = deque()
#             q.append(i)
#             visited[i] = True
# 
#            while(q) :
#                ni = q.popleft()

#                 for j in rooms[ni] :
#                   if visited[j] == True :
#                        continue

#                    visited[j] = True
#                    q.append(j)



#        l = len(rooms)
#        cnt = 0
#        visited = [False] * (l+1)
#        for i in range(l) :
#            if len(rooms[i]) == 0 :
#                continue
#            if visited[i] == False :
#                bfs(i, visited)
#                cnt += 1
#                if cnt > 1 :
#                    return False

#        return True
        
        
from collections import deque
from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def bfs(i, visited) :
            q = deque()
            q.append(i)
            visited[i] = True

            while(q) :
                ni = q.popleft()

                for j in rooms[ni] :
                    if visited[j] == True :
                        continue

                    visited[j] = True
                    q.append(j)



        l = len(rooms)
        visited = [False] * (l+1)
        bfs(0, visited)
        for i in range(l) :
            if visited[i] == False :
                return False
        return True
