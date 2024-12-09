class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [None] * (4 * self.n)  # Each node stores (first_parity, last_parity, is_special)
        self.build(arr, 0, 0, self.n - 1)
    
    def build(self, arr, node, start, end):
        if start == end:
            # Leaf node stores (parity, parity, True)
            self.tree[node] = (arr[start], arr[start], True)
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            self.build(arr, left_child, start, mid)
            self.build(arr, right_child, mid + 1, end)
            self.tree[node] = self._merge(self.tree[left_child], self.tree[right_child])
    
    def _merge(self, left, right):
        # Merge two nodes
        if left == (None, None, True):
            return right  # If left is neutral, return right
        if right == (None, None, True):
            return left  # If right is neutral, return left
        # Merge two nodes
        first_parity = left[0]
        last_parity = right[1]
        is_special = left[2] and right[2] and (left[1] != right[0])  # Adjacent parities must differ
        return (first_parity, last_parity, is_special)
    
    def query(self, L, R, node, start, end):
        if R < start or L > end:
            # No overlap
            return (None, None, True)  # Neutral for merging
        if L <= start and end <= R:
            # Complete overlap
            return self.tree[node]
        if start == end:  # Single element range
            return self.tree[node]
        # Partial overlap
        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2
        left_result = self.query(L, R, left_child, start, mid)
        right_result = self.query(L, R, right_child, mid + 1, end)
        return self._merge(left_result, right_result)
    
    def range_query(self, L, R):
        """Public method to query a range."""
        return self.query(L, R, 0, 0, self.n - 1)[2]  # Return only the is_special value

class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:

        parity = []
        for num in nums:
            parity.append(num%2)

        segTree = SegmentTree(parity)

        result = []

        for L,R in queries:
            isSpecial = segTree.range_query(L,R)
            result.append(isSpecial)
        return result