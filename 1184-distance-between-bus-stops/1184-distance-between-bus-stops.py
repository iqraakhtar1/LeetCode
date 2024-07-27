class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        clockwise_distance = 0
        n = len(distance)
        i = start
        
        while i != destination:
            clockwise_distance += distance[i]
            start += 1
            i = start % n
        
        anticlockwise_distance = sum(distance) - clockwise_distance
        
        return min(clockwise_distance, anticlockwise_distance)
    
#     clockwise_dist = 0
        
#         if start < destination:
#             for i in range(start, destination):
#                 clockwise_dist += distance[i]
#         elif destination < start:
#             for i in range(start-1, destination-1, -1):
#                 clockwise_dist += distance[i]
                
#         total_dist = sum(distance)
        
#         anti_clock_dist = total_dist - clockwise_dist
        
#         return min(anti_clock_dist, clockwise_dist)