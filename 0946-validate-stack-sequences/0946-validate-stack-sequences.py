class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        x = 0
        for i in pushed:
            stack.append(i)
            while stack and stack[-1] == popped[x]:
                stack.pop()
                x+=1
            
        return not stack
            
            
        