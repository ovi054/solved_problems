class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        currentTime = 0
        diff = 0
        for arrival, time in customers:
            if currentTime<arrival:
                currentTime = arrival
            currentTime = currentTime + time
            diff = diff + currentTime - arrival 
        return diff/len(customers)
        