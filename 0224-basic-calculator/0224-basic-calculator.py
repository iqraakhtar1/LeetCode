class Solution:
    def calculate(self, s: str) -> int:
        # Time complexity = O(n), Space complexity = O(n) where n = number of characters in s
        # res of the current paranthesis, and the sign of the previous operation(+ or -)
        # 1 means we are adding, -1 means we are substracting
        stack_of_res = [[0, 1]]
        num = 0
        for i, c in enumerate(s):
            # Ignore space
            if s[i] == ' ':
                continue

            # Keep updating the num until we see an operator or a closing paranthesis
            # Space will be ignored and we know for sure that the experssion is valid
            # So we don't need to worry about 2 2 + 2 which will become 22 using the following logic
            # But it wont happen 2 + (2) - After 2, we can only expect a space or operator or )
            # (1 + 2 )
            if c.isdigit():
                num = num * 10 + int(c)
                continue

            # If c is an opening paranthesis => we have a start of a new expression
            if c == '(':
                stack_of_res.append([0, 1])
                continue

            # Evaluate whatever num when we see a + or - or )
            if c in '+-)':
                # There is a num when you close the paranthesis that we need to first
                # add to our result which is the same as seeing a new operator
                stack_of_res[-1][0] += stack_of_res[-1][1] * num
                stack_of_res[-1][1] = 1 if c == '+' else -1
                num = 0 if c in '+-' else stack_of_res.pop()[0]
                continue
            
        if num != 0:
            stack_of_res[-1][0] += stack_of_res[-1][1] * num

        return stack_of_res[0][0]