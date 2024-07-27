class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(len(nums)-1, 1, -1):
            if nums[i-2] == nums[i-1] == nums[i]:
                nums.pop(i)
        return len(nums)
       
        
        