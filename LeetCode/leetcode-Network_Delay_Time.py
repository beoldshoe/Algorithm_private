from collections import defaultdict
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # graph 생성
        graph = defaultdict(list)
        for n1, n2, sec in times:
            graph[n1].append((n2, sec))
            
        Q = [(0, k)]
        dist = defaultdict(int)
        
        while Q:
            time, node = heapq.heappop(Q)
            if node not in dist:
                dist[node] = time
                for n2, sec in graph[node]:
                    alt = time + sec
                    heapq.heappush(Q, (alt, n2))
                    
        if len(dist) == n:
            return max(dist.values())
        return -1
    
# 참고 블로그
# https://velog.io/@eunseokim/40.-Network-Delay-Time