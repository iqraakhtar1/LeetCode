class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)): 
           for j in range(0, len(nums)):  
                count =  nums[i] + nums[j]
                if count == target and i!=j  :

                    return [i , j]


        