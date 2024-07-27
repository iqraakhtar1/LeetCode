class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = Counter(nums).most_common()
        return ans[0][0]
        
        
        
      