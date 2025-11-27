class Solution:
    def singleNumber(self, nums):
        result = 0
        
        for i in range(32):
            temp = 1 << i
            countOne = 0
            countZero = 0
            
            for num in nums:
                if (num & temp) == 0:
                    countZero += 1
                else:
                    countOne += 1
            
            if countOne % 3 == 1:
                result |= temp
        
        # Handle negative numbers (32-bit signed)
        if result >= 2**31:
            result -= 2**32
        
        return result
