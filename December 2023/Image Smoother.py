class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m = len(img)
        n = len(img[0])
        out = []
        for i in range(m):
            out.append([])
            for j in range(n):
                out[i].append(0)
        for i in range(m):
            for j in range(n):
                sumVal = 0
                count = 0
                for p in range(-1,2):
                    for q in range(-1,2):
                        if i+p<0 or i+p>=m or j+q<0 or j+q>=n:
                            continue
                        sumVal += img[i+p][j+q]
                        count += 1
                out[i][j] = floor(sumVal/count)
        return out