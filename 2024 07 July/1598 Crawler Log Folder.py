class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0
        for log in logs:
            if log == "../":
                count = max(count - 1, 0)
            elif log == "./":
                count = count
            else:
                count = count + 1
        return count
        