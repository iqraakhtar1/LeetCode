class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        def getIndex(val, start):
            end = len(nums2)-1
            while start <= end:
                mid = (start + end)//2
                if nums2[mid] >= val:
                    start = mid+1
                else:
                    end = mid-1
            
            return start-1
        
        dist = 0
        
        for i in range(len(nums1)):
            n = nums1[i]
            j = getIndex(n, i)
            
            dist = max(dist, j-i)
        
        return dist
            
        