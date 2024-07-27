class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        
        ele = []
        for i in range(len(nums)):
            ele.append(nums[i]-i)
        
        dic = {}
        for n in ele:
            if n in dic:
                dic[n] += 1
            else:
                dic[n] = 1
        
        n = len(nums)
        expected_ans = n*(n-1)//2
        
        for k, v in dic.items():
            if v > 1:
                expected_ans -= v*(v-1)//2
        
        return expected_ans