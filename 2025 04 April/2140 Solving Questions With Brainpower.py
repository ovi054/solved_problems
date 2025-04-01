class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        memo = {}
        def solve(i):
            if i>=n:
                return 0
            if i in memo:
                return memo[i]
            pick = questions[i][0] + solve(i+questions[i][1]+1)
            skip = solve(i+1)
            memo[i] = max(pick, skip)
            return memo[i]

        return solve(0)
        