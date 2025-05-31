from collections import deque
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def bfs(x, y, visited) :
            q = deque()
            q.append((x, y))
            visited[x][y] = True

            dx = [0, 0, 1, -1]
            dy = [1, -1, 0 ,0]

            while(q) :
                x1, y1 = q.popleft()
                for i in range(4) :
                    nx = x1 + dx[i]
                    ny = y1 + dy[i]
                    if nx >=m or ny >=n or nx < 0 or ny < 0 : continue
                    if visited[nx][ny] == True : continue
                    if grid[nx][ny] == "0" : continue
                    visited[nx][ny] = True
                    q.append((nx, ny))
        cnt = 0
        visited = [[False] * n for _ in range(m)]
        for i in range(m) :
            for j in range(n) :
                if visited[i][j] == True : continue
                if grid[i][j] == "0" : continue
                bfs(i, j, visited)
                cnt += 1

        return cnt