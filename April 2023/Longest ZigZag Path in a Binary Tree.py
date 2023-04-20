# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        memoL = {}
        memoR = {}
        def dfs(node, cur):
            value = 0
            if(node==None):
                value = 0
            elif(cur == 'left'and node in memoL):
                value = memoL[node]
            elif(cur == 'right'and node in memoR):
                value = memoR[node]
            elif(cur=='left'):
                value = 1 + dfs(node.right,'right')
                memoL[node] = value
            elif(cur=='right'):
                value = 1 + dfs(node.left,'left')
                memoR[node] = value
            return value
        global maxVal
        maxVal = 0
        def traverse(node):
            if(node==None):
                return
            global maxVal
            maxVal = max(maxVal,dfs(node,'left')-1)
            maxVal = max(maxVal,dfs(node,'right')-1)
            traverse(node.left)
            traverse(node.right)
            return maxVal
        return traverse(root)