# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        if not root1 and not root2:
            return True
        
        if not root1 or not root2:
            return False
        
        global check
        check = []
        def inOrderTraversal(root):
            global check
            if root:
                inOrderTraversal(root.left)
                if not root.left and not root.right:
                    check.append(root.val)
                
                inOrderTraversal(root.right)
                
        inOrderTraversal(root1)
        ind2 = len(check)
        inOrderTraversal(root2)
        ind1 = 0
        
        if len(check)%2 != 0:
            return False
                
        while ind2 < len(check):
            if check[ind1] != check[ind2]:
                return False
            ind1 += 1
            ind2 += 1
            
        return True