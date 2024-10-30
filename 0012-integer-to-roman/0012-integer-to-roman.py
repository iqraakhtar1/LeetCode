class Solution:
    def intToRoman(self, num: int) -> str:
        symbol_list = [['M', 1000], ['CM', 900], ['D', 500], ['CD', 400], ['C', 100],['XC', 90],
                       ['L', 50], ['XL', 40], ['X', 10], ['IX', 9], ['V', 5], ['IV', 4], ['I', 1]]
        output = ''
        for symbol, number in symbol_list:
            count = num//number
            output += (symbol*count)
            num = num%number
                
        return output
        
#         ans = ""
        
#         if num >= 1000:
#             cnt = num//1000
#             ans += (cnt*dic[1000])
#             num = num%1000
        
#         if num >= 900:
#             cnt = num//900
#             ans += (cnt*dic[900])
#             num = num%900
            
#         if num >= 500:
#             cnt = num//500
#             ans += (cnt*dic[500])
#             num = num%500
        
#         if num >= 400:
#             cnt = num//400
#             ans += (cnt*dic[400])
#             num = num%400
        
#         if num >= 100:
#             cnt = num//100
#             ans += (cnt*dic[100])
#             num = num%100
                
#         if num >= 90:
#             cnt = num//90
#             ans += (cnt*dic[90])
#             num = num%90
        
#         if num >= 50:
#             cnt = num//50
#             ans += (cnt*dic[50])
#             num = num%50
        
#         if num >= 40:
#             cnt = num//40
#             ans += (cnt*dic[40])
#             num = num%40
        
#         if num >= 10:
#             cnt = num//10
#             ans += (cnt*dic[10])
#             num = num%10
            
#         if num >= 9:
#             cnt = num//9
#             ans += (cnt*dic[9])
#             num = num%9
        
#         if num >= 5:
#             cnt = num//5
#             ans += (cnt*dic[5])
#             num = num%5
        
#         if num >= 4:
#             cnt = num//4
#             ans += (cnt*dic[4])
#             num = num%4
        
#         if num >= 1:
#             ans += (num*dic[1])
#             num = 0
        
#         return ans
            