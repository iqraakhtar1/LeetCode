class Solution:
     def canJump(self, nums: List[int]) -> bool:
        res = len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if i+nums[i]>=res:
                res=i
        return True if res==0 else False
            
                
            
        