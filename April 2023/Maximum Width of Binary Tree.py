# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = deque([(root,0)])
        max_length = 0
        while queue:
            level_length = len(queue)
            # print(queue[0])
            _,start_index = queue[0]
            _,end_index = queue[-1]
            for i in range(level_length):
                node, index = queue.popleft()
                if(node.left):
                    queue.append((node.left,2*index))
                if(node.right):
                    queue.append((node.right,2*index+1))
            max_length = max(max_length,end_index-start_index+1)
        return max_length