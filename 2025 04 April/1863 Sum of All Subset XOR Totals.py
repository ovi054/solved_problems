class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        subsets = []
        n = len(nums)

        def solve(i,curSubset):
            if i>=n:
                subsets.append(curSubset)
                return 

            curSubset2 = curSubset.copy()
            curSubset2.append(nums[i])
            solve(i+1, curSubset2)
            solve(i+1, curSubset)

        solve(0,[])
        output = 0
        for subset in subsets:
            val = 0
            for s in subset:
                val = val^s
            output+=val

        return output


        