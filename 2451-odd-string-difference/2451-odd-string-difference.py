class Solution:
    def oddString(self, words: List[str]) -> str:
        dic = {
 'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9,
 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18,
 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25
}
        dic2 = {}
        for word in words:
            temp = []
            for i in range(len(word)-1):
                temp.append(dic[word[i]]-dic[word[i+1]])
            
            if tuple(temp) in dic2:
                dic2[tuple(temp)].append(word)
                
            else:
                dic2[tuple(temp)]=[word]
        
        for key,value in dic2.items():
            if len(value) == 1:
                return value[0]
                
                
        
        
            
                
            
                
                
                
                
        
        
        
        