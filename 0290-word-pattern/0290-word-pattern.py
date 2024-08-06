class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        map = {}
        s = s.split(" ")
        if len(pattern) != len(s):
            return False
        if len(set(pattern)) != len(set(s)):
            return False
        for i in range(len(s)):
            if s[i] not in map:
                map[s[i]] = pattern[i]
            elif map[s[i]] != pattern[i]:
                return False
        return True
            
    
        