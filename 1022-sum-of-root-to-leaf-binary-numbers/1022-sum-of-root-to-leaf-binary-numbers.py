# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        
        def calculateDecimal(binary):
            ans = 0
            power = 0
            for i in range(len(binary)-1, -1, -1):
                ans += int(binary[i])*(2**power)
                power += 1
            
            return ans
        
        stack = [[root, ""]]
        ans = 0
        while stack:
            
            node, bin_num = stack.pop()
            
            bin_num += str(node.val)
            
            if not node.left and not node.right:
                dec_num = calculateDecimal(bin_num)
                ans += dec_num
                
            if node.right:
                stack.append([node.right, bin_num])
                
            if node.left:
                stack.append([node.left, bin_num])
        
        return ans