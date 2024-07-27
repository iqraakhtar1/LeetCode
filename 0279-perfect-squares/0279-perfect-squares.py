class Solution:
    def numSquares(self, n: int) -> int:
    
        rec = [float("inf")] * (n + 1)
        rec[0] = 0
        for i in range(1, n+1):
            
            smaller = float("inf")
            num = 1
            while num * num <= i:
                smaller = min(smaller, rec[i-num*num]+1)
                num += 1

            rec[i] = smaller
            
        return rec[n]
    