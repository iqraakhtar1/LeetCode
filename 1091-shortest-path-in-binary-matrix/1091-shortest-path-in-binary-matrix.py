class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        directions = [(0,1), (-1,0), (1,0), (0,-1), (1,1), (-1,-1), (1,-1), (-1,1)]
        m, n = len(grid), len(grid[0])
        if m == 0 or n ==0 or grid[0][0]!=0:
            return -1
        def is_safe(x: int, y:int)-> bool:
            return 0<=x < m and 0<=y<n
        
        result = [[float('inf')]*n for _ in range(n)]
        pq =[(0, 0, 0)]
        result[0][0] = 0
        while pq:
            d, x, y = heappop(pq)
            for dx, dy in directions:
                x_, y_ = x+dx, y+dy
                dist = 1
                if is_safe(x_, y_) and grid[x_][y_] == 0 and d+dist< result[x_][y_]:
                    heappush(pq, (d+dist, x_, y_))
                    grid[x_][y_]=1
                    result[x_][y_] = d+dist
        if result[m-1][n-1] == float('inf'):
            return -1
        return result[m-1][n-1]+1
        

        
#         n = len(grid)
        
#         if grid[0][0] == 1 or grid[n-1][n-1]==1:
#             return -1
        
        
        # directions = [(0,1), (-1,0), (1,0), (0,-1), (1,1), (-1,-1), (1,-1), (-1,1)]
        
#         visited = set()
        
#         queue = collections.deque([(0,0,0)])
        
#         while queue:
#             x, y, dist = queue.popleft()
            
#             if x == n-1 and y == n-1:
#                 return dist+1
            
#             for direction in directions:
#                 next_x, next_y, new_dist = direction[0] + x, direction[1] + y, dist+1
                
#                 if next_x >= 0 and next_x < n and next_y >= 0 and next_y < n and grid[next_x][next_y] != 1 and (next_x,next_y) not in visited:
#                     queue.append((next_x, next_y, new_dist))
#                     visited.add((next_x, next_y))
        
#         return -1
            