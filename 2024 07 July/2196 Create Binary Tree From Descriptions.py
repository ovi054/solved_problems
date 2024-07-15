# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        hashTable = defaultdict(list)
        for node,child, isLeft in descriptions:
            if(node not in hashTable):
                hashTable[node] = [-1,-1]
            hashTable[node][isLeft] = child
        
        keys_dict = defaultdict(int)
        for key in hashTable:
            keys_dict[key] = 1

        for key in hashTable:
            keys_dict.pop(hashTable[key][0], None)
            keys_dict.pop(hashTable[key][1], None)
        
        rootVal = list(keys_dict.keys())[0]
        rootNode = TreeNode(rootVal)
        node = rootNode
        
        def creteChildTree(node):
            if(node.val not in hashTable):
                return
            elif(hashTable[node.val][0]==-1 and hashTable[node.val][1]==-1):
                return
            if(hashTable[node.val][0]!=-1):
                node.right = TreeNode(hashTable[node.val][0])
                creteChildTree(node.right)
            if(hashTable[node.val][1]!=-1):
                node.left = TreeNode(hashTable[node.val][1])
                creteChildTree(node.left)
        
        creteChildTree(node)
        return rootNode