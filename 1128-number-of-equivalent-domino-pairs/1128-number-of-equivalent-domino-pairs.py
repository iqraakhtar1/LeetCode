class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        #byusing combination formula nCr
        
        dic = {}
        
        for d in dominoes:
            if (d[0], d[1]) in dic:
                dic[(d[0], d[1])] += 1
                
            elif (d[1], d[0]) in dic:
                dic[(d[1], d[0])] += 1
                
            else:
                dic[(d[0], d[1])] = 1
        
        def calculate(n):
            
            numirator = 1
            denominator = 1
            
            for i in range(1, n+1):
                numirator *= i
            
            for i in range(1, n-1):
                denominator *= i
            
            denominator *= 2
            
            return numirator//denominator
        
        ans = 0
        for k, v in dic.items():
            if v > 1:
                ans += calculate(v)
        
        return ans