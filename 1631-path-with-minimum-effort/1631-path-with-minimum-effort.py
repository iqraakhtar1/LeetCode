class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        directions = [
            (-1, 0),
            (0, -1), (0, 1),
            (1, 0)
            ]
        
        m = len(heights)
        n = len(heights[0])
        def is_safe(x, y):
            return 0<=x<m and 0<=y<n
        result = [[float('inf')]*n for _ in range(m)]
        pq = [(0, 0, 0)]
        result[0][0] = 0
        while pq:
            diff, x, y = heappop(pq)
            if x == m-1 and y == n-1:
                return diff
            for dx, dy in directions:
                x_, y_ = x+dx, y+dy

                if is_safe(x_, y_):
                    abs_diff= max(diff, abs(heights[x][y] - heights[x_][y_]))
                    if result[x_][y_]>abs_diff:
                        result[x_][y_] = abs_diff
                        heappush(pq, (result[x_][y_], x_, y_))
        return result[m-1][n-1]
            
        