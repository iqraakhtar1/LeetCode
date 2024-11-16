class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        length = 0
        for n in nums:
            if (n-1) not in numSet:
                longest = 0
                while(n+longest) in numSet:
                    longest+=1
                length = max(length, longest)
        return length
                    