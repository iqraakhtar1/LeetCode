class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        ans = []
        for i in range(len(nums)):
            sum += nums[i]
            ans.append(sum)
        return ans
       
        