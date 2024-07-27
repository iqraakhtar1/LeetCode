class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit +=prices[i] - prices[i-1]
        return profit
            
        # l, r = 0, 1
        # arr = []
        # sumi = 0
        # while r < len(prices):
        #     if prices[l]<prices[r]:
        #         profit = prices[r] - prices[l]
        #         arr = arr.append(profit)
        #         sumi = sum(profit)
        #         l+=1
        #         r+=1
        #     else:
        #         l = r
        #         r+=1
        # return sumi
        
        