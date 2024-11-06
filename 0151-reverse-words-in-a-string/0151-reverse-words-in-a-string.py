class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])

        # l = 0
        # r = 0
        # _len = len(s)
        # str1 = ""
        # while r <= _len:
        #     if r == _len or s[r] == ' ':
        #         str1 +=' ' + s[l:r][::-1]  #reversing a word over here and adding to a result str1
        #         l = r+1
        #         while l < _len and s[l] == ' ':
        #             l += 1
        #         r = l
        #     r += 1
        # str2 = str1[::-1]
        # str2 = str2.rstrip().lstrip() #stripping space front and back....
        # return str2

        
        
            
        
        