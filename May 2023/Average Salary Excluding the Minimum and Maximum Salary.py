class Solution:
    def average(self, salary: List[int]) -> float:
        salary = sorted(salary)
        sumValue = sum(salary)
        avg = (sumValue - salary[0] -salary[-1])/(len(salary)-2)
        return avg