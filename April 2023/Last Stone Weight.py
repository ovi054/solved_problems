class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = sorted(stones)
        while(len(stones)>1):
            y = stones.pop()
            x = stones.pop()
            if(x!=y):
                bisect.insort_left(stones, y-x)
            # x = stones[-2]
            # y = stones[-1]
            # if(x==y):
            #     stones.pop()
            #     stones.pop()
            # else:
                # add_value = y - x
                # stones.pop()
                # stones.pop()
                # bisect.insort_left(stones, add_value)
        if(len(stones)==0):
            return 0
        else:
            return stones[0]