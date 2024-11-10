class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        words_str = ""
        for word in words:
            words_str +=word
        ans = []
        length = len(words[0])
        l = 0
        r = len(words_str)
        while l < len(s) and r <= len(s):

            temp = []
            tempw = s[l:r]
            for t in range(0,len(tempw),length):
                temp.append(tempw[t:t+length])

            if sorted(temp) == sorted(words):
                ans.append(l)

            l+=1
            r+=1

        return ans
        
        