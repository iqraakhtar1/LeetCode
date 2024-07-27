class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        current = ''
        i = 0
        while i < len(path):
            if path[i] == '/':
                i += 1
                continue
            buffer = ''            
            while i < len(path) and path[i] != '/':
                buffer += path[i]
                i += 1
            if buffer == '.':
                continue
            elif buffer == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(buffer)
            
        return '/'+'/'.join(stack)