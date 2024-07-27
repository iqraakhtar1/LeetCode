class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        col = [""]*len(strs[0])
        for i in range(len(strs)):
            for j in range(len(strs[0])):
                col[j]+=strs[i][j]
        ans = 0
                
        for c in col:
            flag = True
            for i in range(len(c)-1):
                if ord(c[i]) <= ord(c[i+1]):
                    continue
                else:
                    flag = False
                    break
            if flag == False:
                ans+=1
        return ans
        
            
            
        