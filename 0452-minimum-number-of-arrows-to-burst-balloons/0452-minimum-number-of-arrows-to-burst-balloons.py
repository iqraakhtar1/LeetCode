class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points: return 0
        points.sort(key=lambda x:x[1])
        start = points[0][1]
        arrow = 1
        for i in range(1, len(points)):
            first , end = points[i]
            if first > start:
                arrow+=1
                start = end
        return arrow
        
        