class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r= max(weights), sum(weights)
        min_cap= r
        def canShip(Cap):
            ships,Curr_weight=1, Cap

            for w in weights:
                if Curr_weight-w < 0:
                    ships+=1
                    Curr_weight=Cap
                Curr_weight-=w
            return ships <= days

        while l<=r:
            Cap= (l+r)//2
            if canShip(Cap):
                min_cap=min(min_cap,Cap)
                r=Cap-1
            else:
                l=Cap+1
        return min_cap