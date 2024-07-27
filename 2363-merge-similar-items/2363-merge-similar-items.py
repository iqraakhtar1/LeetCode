class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        dic = {}
        for i in range(len(items1)):
            value, weight = items1[i]
            if value in dic:
                dic[value]+=weight
            else:
                dic[value]= weight
        for i in items2:
            value, weight = i
            if value in dic:
                dic[value]+=weight
            else:
                dic[value]= weight
        ans = []
        for key, value in dic.items():
            ans.append([key,value])
        ans.sort()
        return ans
            
        
                
                
        