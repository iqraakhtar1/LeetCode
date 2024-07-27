class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [int(x) for x in version1.split('.')]
        v2 = [int(x) for x in version2.split('.')]

        n = max(len(v1), len(v2))
        for i in range(n):
            v1_val = v1[i] if i < len(v1) else 0
            v2_val = v2[i] if i < len(v2) else 0

            if v1_val < v2_val:
                return -1
            elif v1_val > v2_val:
                return 1

        return 0
        
            
        
       
       
        