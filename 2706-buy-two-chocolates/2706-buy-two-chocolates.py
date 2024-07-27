class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        
        minimum = float('inf')
        sec_min = float('inf')
        
        for i in prices:
            
            if i <= minimum:
                sec_min = minimum
                minimum = i
            
            elif i <= sec_min and i >= minimum:
                sec_min = i
        
        prices = minimum + sec_min 
        
        if prices <= money:
            return money - prices
        else:
            return money
        