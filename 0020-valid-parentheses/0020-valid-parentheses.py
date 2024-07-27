class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeTo = {")":"(", "}":"{","]":"["}
        for c in s:
            if c in closeTo:
                if stack and stack[-1] == closeTo[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
       
                
                    
                
    



        