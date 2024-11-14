class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map1=[]
        map2=[]
        for indx in s:
            map1.append(s.index(indx))
        for indx in t:
            map2.append(t.index(indx))
        if map1 == map2:
            return True
        
        return False
    
     
    
    
    
        
        