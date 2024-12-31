class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        n = len(days)
        def search(target):
            start = 0
            end = n -1
            while(start<=end):
                mid = (start+end)//2
                if days[mid] == target:
                    return mid
                elif(days[mid]<target):
                    start = mid+1
                else:
                    end = mid - 1
            return end+1
        
        memo = {}

        def solve(index, cost):

            if (index,cost) in memo:
                return memo[(index,cost)]

            if(index>=n):
                return cost

            day = solve(index+1, cost+costs[0])
            week = solve(search(days[index]+7), cost+costs[1])
            month = solve(search(days[index]+30), cost+costs[2])

            memo[(index,cost)] = min(day, week, month)
            return memo[(index,cost)]

        return solve(0,0)