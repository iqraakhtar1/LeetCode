class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = nums[0]
        ans = nums[0]
        for i in range(1, len(nums)):
            curr = max(curr+nums[i], nums[i])
            ans = max(ans, curr)
        return ans
            
        
#         sub = nums[0]
#         curr = 0
#         for i in nums:
#             if curr < 0:
#                 curr = 0
#             curr += i
#             maxSub = max(sub, curr)
#         return maxSub
        