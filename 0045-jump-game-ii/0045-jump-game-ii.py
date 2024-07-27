class Solution:
    def jump(self,nums:List[int])->int:
        start , end , count = 0, 0,0
        for i in range(len(nums)-1):
            start = max(start, i+nums[i])
            if end == i:
                end = start
                count+=1
        return count
            
      
       
