# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []
#         closeTo = {")":"(", "}":"{","]":"["}
#         for c in s:
#             if c in closeTo:
#                 if stack and stack[-1] == closeTo[c]:
#                     stack.pop()
#                 else:
#                     return False
#             else:
#                 stack.append(c)
#         return True if not stack else False
       
class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        for c in s:
            if c in '({[':
                st.append(c)
            else:
                if not st or \
                c==')' and st[-1]!='(' or \
                c=='}' and st[-1]!='{' or \
                c==']' and st[-1]!='[':
                    return False
                else:
                    st.pop()
        return not st                
                    
                
    



        