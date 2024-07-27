class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        running_sum = 0
        hash_map = {0:1}
        
        subarrays_count = 0
        
        for i, num in enumerate(nums):
            running_sum += num
            
            if running_sum - k in hash_map:
                subarrays_count += hash_map[running_sum - k]
            
            hash_map[running_sum] = hash_map.get(running_sum, 0) + 1
        
        return subarrays_count