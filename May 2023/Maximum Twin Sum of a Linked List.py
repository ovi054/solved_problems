# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        temp = head
        nodeList = []
        while(temp):
            nodeList.append(temp.val)
            temp = temp.next
        n = len(nodeList)
        maxSum = -99999999999
        for i in range(0,n//2):
            sumValue = nodeList[i] + nodeList[n-1-i]
            if(sumValue>maxSum):
                maxSum = sumValue
        return maxSum
