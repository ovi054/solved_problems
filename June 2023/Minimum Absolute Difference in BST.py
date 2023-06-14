# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import bisect
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        arrList = []
        def dfs(node):
            if( not node):
                return
            bisect.insort(arrList,node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        n, minDifValue = len(arrList), arrList[1] - arrList[0]
        for i in range(1,n):
            diff = abs(arrList[i] - arrList[i-1])
            if(diff<minDifValue):
                minDifValue = diff
        return minDifValue

        
