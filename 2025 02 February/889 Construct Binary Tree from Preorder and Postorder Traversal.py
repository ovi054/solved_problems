# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        def breakSubTree(preorder,postorder):
            if(not preorder):
                return [],[],[],[]
            breakValue = preorder[0]
            k =postorder.index(breakValue)

            preorderL = preorder[:k+1]
            postorderL = postorder[:k+1]

            preoderR = preorder[k+1:]
            postorderR = postorder[k+1:]
            return preorderL, postorderL, preoderR, postorderR


        def constructTree(preorder, postorder, node):

            node.val = preorder[0]
            preorder = preorder[1:]
            postorder = postorder[:len(postorder)-1]
            preoderL, postorderL, preorderR, postorderR = breakSubTree(preorder, postorder)

            if(len(preoderL)>=1):
                left = TreeNode()
                node.left = left
                constructTree(preoderL, postorderL, node.left)

            if(len(preorderR)>=1):
                right = TreeNode()
                node.right = right
                constructTree(preorderR, postorderR, node.right)

        
        root = TreeNode()
        constructTree(preorder, postorder, root)
        return root  