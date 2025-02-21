# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        root.val = 0
        def dfs1(node):
            self.root = root
            if not node:
                return
            
            left = node.left
            if left:
                left.val = node.val*2+1
                dfs1(left)
            right = node.right
            if right:
                right.val = node.val*2+2
                dfs1(right)

        dfs1(root)

        

    def find(self, target: int) -> bool:
        def dfs(node):
            if not node:
                return False
            if node.val==target:
                return True

            a = False
            b = False
            if target>node.val:
                a = dfs(node.left)
                b = dfs(node.right)
            return a or b


        return dfs(self.root)
            
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)