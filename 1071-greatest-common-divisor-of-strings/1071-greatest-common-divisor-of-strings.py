class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2 != str2+str1:
            return ""
        
        s1 = len(str1)
        s2 = len(str2)
        while s1!=s2:
            if s1>s2:
                s1-=s2
            else:
                s2-=s1
        return str1[:s1]