# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(node, depth):
            if not node:
                return None, depth

            left, leftDepth = dfs(node.left, depth+1)
            right, rightDepth = dfs(node.right, depth+1)

            if leftDepth>rightDepth:
                return left, leftDepth
            elif rightDepth>leftDepth:
                return right, rightDepth
            else:
                return node, rightDepth

        output,_ = dfs(root,0)
        return output
        