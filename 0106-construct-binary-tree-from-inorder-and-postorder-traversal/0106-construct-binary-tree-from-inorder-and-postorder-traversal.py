# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        global i
        i = len(postorder)-1
        def helper(inorder, postorder, start, end):
            global i
            if i < 0 or start > end:
                return None
            
            ele = postorder[i]
            i -= 1
            
            ind = inorder.index(ele)
            
            node = TreeNode(ele)
            node.right = helper(inorder, postorder, ind+1, end)
            node.left = helper(inorder, postorder, start, ind-1)
            return node
        
        return helper(inorder, postorder, 0, len(postorder)-1)
        
        