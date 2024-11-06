class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == "":
            return 0
        i=0
        while i<len(haystack):
            if haystack[i:i+len(needle)]==needle:
                return i
            i+=1
        return -1
        
        
        
        
        