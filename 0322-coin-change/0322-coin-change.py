class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        
        def getCoins(coins, amount, memo):
            
            if amount < 0:
                return float("inf")
            
            if amount == 0:
                return 0
            
            if amount in memo:
                return memo[amount]
            
            coinsPicked = float("inf")
            for i in range(len(coins)):
                coin = coins[i]
                output = getCoins(coins, amount - coin, memo)
                
                if output != float("inf"):
                    coinsPicked = min(output+1, coinsPicked)
                    
            memo[amount] = coinsPicked
            
            return memo[amount]
        
        memo = {}
        
        ans = getCoins(coins, amount, memo)
        
        if ans == float("inf"):
            return -1
        
        return ans