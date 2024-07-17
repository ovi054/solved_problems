# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete_set = set(to_delete)
        result = []
        def dfs(node,isRoot):
            if not node:
                return None
            isDeleted = node.val in to_delete_set
            if(isRoot and not isDeleted):
                result.append(node)
            node.left = dfs(node.left,isDeleted)
            node.right = dfs(node.right,isDeleted)
            return None if isDeleted else node 
        dfs(root,True)
        return result