# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(not head or not head.next):
            return head
        dummy = ListNode(0)
        dummy.next =  head
        cur = dummy
        while(cur.next and cur.next.next):
            node1 = cur.next
            node2 = cur.next.next
            cur.next = node2
            temp = node2.next
            node2.next = node1
            node1.next = temp
            cur = node1
        return dummy.next
