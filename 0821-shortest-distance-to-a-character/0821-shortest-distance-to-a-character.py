class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        
        occurrences = []
        for i in range(len(s)):
            if s[i] == c:
                occurrences.append(i)
        
        ans = []
        
        for i in range(len(s)):
            if s[i] == c:
                ans.append(0)
            else:
                temp = []
                for j in range(len(occurrences)):
                    temp.append(abs(occurrences[j]-i))
                
                min_dist = min(temp)
                ans.append(min_dist)
        
        return ans