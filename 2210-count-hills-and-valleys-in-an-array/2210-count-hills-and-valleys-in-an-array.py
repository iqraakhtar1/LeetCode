class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        
        ans = 0

        for i in range(1, len(nums)- 1):
            if nums[i] == nums[i+1]:  # Same Hill or Valley
                nums[i] = nums[i-1]
                
            elif nums[i] > nums[i-1] and nums[i] > nums[i+1]:  # Hill
                ans += 1
                
            elif nums[i] < nums[i-1] and (nums[i] < nums[i+1]):  # Valley
                ans += 1 
                
        return ans