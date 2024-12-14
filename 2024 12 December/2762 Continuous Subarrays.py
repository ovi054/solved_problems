from sortedcontainers import SortedDict
class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        i, j = 0, 0
        n = len(nums)

        sortedDict = SortedDict()

        sortedDict[nums[j]] = 1

        count = 0
        while(i>=0 and j>=0 and i<n and j<n):
            minValue = sortedDict.iloc[0]
            maxValue = sortedDict.iloc[-1]
            if((maxValue-minValue)<=2):
                count += j-i+1
                j+=1
                if j<n:
                    if nums[j] in sortedDict:
                        sortedDict[nums[j]] += 1
                    else:
                        sortedDict[nums[j]] = 1
            else:
                if sortedDict[nums[i]]>1:
                    sortedDict[nums[i]]-=1
                else:
                    del sortedDict[nums[i]]
                i+=1
        return count
