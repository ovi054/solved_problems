# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:

        def find(node, target, path=[]):
            if node.val==target:
                return True
            if(node.left and find(node.left,target, path)):
                path.append('L')
            elif(node.right and find(node.right,target, path)):
                path.append('R')
            return path
        node = root
        leftPath, rightPath = [],[]
        find(node, startValue, leftPath)
        find(node, destValue, rightPath)

        while(len(leftPath) and len(rightPath) and leftPath[-1]==rightPath[-1]):
            leftPath.pop()
            rightPath.pop()
        return ''.join('U'*len(leftPath)) + ''.join(reversed(rightPath))
        