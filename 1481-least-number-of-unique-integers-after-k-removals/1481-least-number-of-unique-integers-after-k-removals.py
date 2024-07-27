class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        
        dic = {}   #  key : value
        
        for n in arr:
            if n in dic:
                dic[n] += 1
                
            else:
                dic[n] = 1
                
        numbers = []
        for key, value in dic.items():
            numbers.append((value,key))
        
        numbers.sort(reverse=True)
        
        uniq = 0
        while k > 0:
            top_ele = numbers.pop()
            if top_ele[0] == 1:
                k -= 1
            else:
                if k < top_ele[0]:
                    k -= top_ele[0]
                    uniq += 1
                else:
                    k -= top_ele[0]
        
        return len(numbers) + uniq
                    
        