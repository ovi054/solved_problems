class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        n = len(queries)
        res = [-1]*n
        group = defaultdict(list)
        for index,q in enumerate(queries):
            l, r = sorted(q)
            if l==r or heights[r]>heights[l]:
                res[index] = r
            else:
                group[r].append((max(heights[l],heights[r]),index))
        heap = []
        for i, h in enumerate(heights):
            for q_h, q_i in group[i]:
                heappush(heap,(q_h, q_i))

            while heap and h>heap[0][0]:
                q_h, q_i = heappop(heap)
                res[q_i] = i
        return res