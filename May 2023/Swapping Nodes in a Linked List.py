# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head
        valueList = []
        while(temp):
            valueList.append(temp.val)
            temp = temp.next
        n = len(valueList)
        print(valueList)
        k = k - 1
        tempValue = valueList[k]
        valueList[k] = valueList[n-k-1]
        valueList[n-k-1] = tempValue

        dummy = ListNode(0)
        cur = dummy
        for value in valueList:
            cur.next = ListNode(value)
            cur = cur.next
        return dummy.next

