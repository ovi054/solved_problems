# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head_n = ListNode(0)
        current = head_n
        val = 0
        node = head.next
        while(node):
            if(node.val!=0):
                val = val + node.val
            else:
                current.next = ListNode(val)
                current = current.next
                val = 0
            node = node.next
        return head_n.next


        