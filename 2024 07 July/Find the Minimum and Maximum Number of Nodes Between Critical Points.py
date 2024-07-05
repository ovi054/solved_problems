# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        criticalPoints = []
        node = head
        prev = None
        prevVal = 0
        index = 1
        while(node):
            if(prev and node.next):
                if node.val<prevVal and node.val<node.next.val:
                    criticalPoints.append(index)
                elif node.val>prevVal and node.val>node.next.val:
                    criticalPoints.append(index)
            prev = node
            prevVal = node.val
            index+=1
            node = node.next
        output =[-1,-1]
        n = len(criticalPoints)
        if(n>1):
            minVal = 99999999
            for i in range(1,n):
                distance = criticalPoints[i] - criticalPoints[i-1]
                if(distance<minVal):
                    minVal = distance
            maxVal = criticalPoints[n-1] - criticalPoints[0]
            output[0] = minVal
            output[1] = maxVal
        return output