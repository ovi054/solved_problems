#tags: binary search
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions = sorted(potions, reverse =True)
        size = len(potions)
        def search(mulValue,x):
            start = 0
            end = size - 1
            while(start<=end):
                mid = (start+end)//2
                #ignored (==x) as list can contains same multiple value
                # if(potions[mid]*mulValue==x):
                #     # print(size,mid)
                #     return mid + 1
                if(potions[mid]*mulValue>=x):
                   start = mid + 1
                else:
                    end = mid - 1
            # print(size, end+1)
            return end+1
        output = []
        for spell in spells:
            output.append(search(spell,success))
        return output