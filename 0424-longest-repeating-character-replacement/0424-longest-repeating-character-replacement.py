class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        Count ={}
        res = 0
        l = 0
        for r in range(len(s)):
            Count[s[r]] = 1+Count.get(s[r], 0)
            if (r - l +1) - max(Count.values()) > k:
                Count[s[l]] -=1
                l+=1
            res = max(res, r-l+1)
        return res
       