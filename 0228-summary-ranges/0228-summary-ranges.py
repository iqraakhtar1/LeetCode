class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        l,r = 0, 0
        ans = []
        while r < len(nums):
            while r + 1 < len(nums) and nums[r+1] == nums[r]+1:
                r += 1
            
            if l == r:
                ans.append(str(nums[l]))
            else:
                ans.append(str(nums[l]) + "->" + str(nums[r]))
            r += 1
            l = r
        
        return ans
       
        