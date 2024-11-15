class Solution:
     def isAnagram(self, s: str, t: str) -> bool:
            if len(s)!=len(t):
               return False
            countS , countT = {},{}
            for i in range(len(s)):
                countS[s[i]] = 1+countS.get(s[i], 0)
                countT[t[i]] = 1+countT.get(t[i], 0)
            for c in countS:
                if countS[c] != countT.get(c, 0):
                    return False
            return True

            
#             char_count = [0]*26
#             for char in s:
#                 char_count[ord(char) - ord('a')]+=1
                
#             for char in t:
#                 char_count[ord(char) - ord('a')]-=1
#                 if char_count[ord(char) - ord('a')] < 0:
#                     return False
#             return True

            
            
        
            
            
       
        
        