class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i == (len(s)) or s[i] != strs[0][i]:
                    return res
            res+=s[i]
        return res
            
       
        # p=""   
        # if len(strs)==0:
        #     return p
        # strs = sorted(strs)
        # for i in range(len(min(strs))):
        #     c=strs[0][i]
        #     if strs[-1].startswith(p+c):
        #         p+=c
        #     else:
        #         break
        # return p