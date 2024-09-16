# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []

        def dfs(node, level):
            if not node:
                return

            # If this is the first time we're visiting this level
            if level == len(res):
                res.append(node.val)

            # First go right, then left
            dfs(node.right, level + 1)
            dfs(node.left, level + 1)

        dfs(root, 0)
        return res

#     def rightSideView(self, root: TreeNode) -> List[int]:
#         res = []
#         q = collections.deque([root])

#         while q:
#             rightSide = None
#             qLen = len(q)

#             for i in range(qLen):
#                 node = q.popleft()
#                 if node:
#                     rightSide = node
#                     q.append(node.left)
#                     q.append(node.right)
#             if rightSide:
#                 res.append(rightSide.val)
#         return res