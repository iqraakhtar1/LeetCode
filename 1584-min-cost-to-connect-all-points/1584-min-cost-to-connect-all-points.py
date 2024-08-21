class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        V = len(points)
        adj = [[] for _ in range(V)]

        for i in range(V):
            for j in range(i + 1, V):
                x1, y1 = points[i]
                x2, y2 = points[j]
                d = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append((j, d))
                adj[j].append((i, d))

        return self.minMST(adj, V)
    
    def minMST(self, adj, V):
        pq = [(0, 0)]  # priority queue: (weight, vertex)
        inMST = [False] * V
        sumCost = 0
        
        while pq:
            wt, node = heapq.heappop(pq)
            if inMST[node]:
                continue
            
            inMST[node] = True
            sumCost += wt
            
            for neighbor, neighbor_wt in adj[node]:
                if not inMST[neighbor]:
                    heapq.heappush(pq, (neighbor_wt, neighbor))
        
        return sumCost
