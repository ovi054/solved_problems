# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node,outList=[]):
            if node.left==None and node.right==None:
                outList.append(node.val)
            if node.left:
                dfs(node.left,outList)
            if node.right:
                dfs(node.right,outList)
            return outList
        if dfs(root1,[]) == dfs(root2,[]):
            return True
        else:
            return False
        