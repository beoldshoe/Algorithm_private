from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 :
            return -1
        
        l = len(grid)

        visited = [[False] * l for _ in range(l)]

        q = deque()
        q.append((0,0,1))
        visited[0][0] = True

        dx = [-1, 1, 0, 0, 1, 1, -1, -1]
        dy = [0, 0 ,1, -1, 1, -1, 1, -1]

        while(q) :
            x1, y1, cnt = q.popleft()
            if x1 == l-1 and y1 == l-1 :
                return cnt
            for i in range(8) :
                nx = dx[i] + x1
                ny = dy[i] + y1

                if nx < 0 or ny < 0 or nx >= l or ny >= l : continue
                if visited[nx][ny] == True : continue
                if grid[nx][ny] == 1 : continue

                visited[nx][ny] = True
                q.append((nx,ny,cnt+1))

        return -1



