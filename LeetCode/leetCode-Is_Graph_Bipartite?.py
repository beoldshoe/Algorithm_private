from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [0] * n   # 0: 미방문, 1/-1: 두 색

        for i in range(n):
            if color[i] != 0:
                continue
            # BFS 시작
            queue = deque([i])
            color[i] = 1
            while queue:
                u = queue.popleft()
                for v in graph[u]:
                    if color[v] == 0:  # 아직 안 칠했으면 반대 색
                        color[v] = -color[u]
                        queue.append(v)
                    elif color[v] == color[u]:  # 같은 색이면 이분 그래프 아님
                        return False
        return True
