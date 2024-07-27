class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        
        while left <= right:
            flag = False
            for rng in ranges:
                l, r = rng
                
                if left >= l and left <= r:
                    flag = True
                    break
            
            if flag == False:
                return False
        
            left += 1
            
        return True