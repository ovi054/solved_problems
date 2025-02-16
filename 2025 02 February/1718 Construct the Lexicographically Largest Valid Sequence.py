class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        
        used = [False]*(n+1)
        arr = [-1]*(n*2-1)
        def solve(index, n, used, arr):

            if index>=len(arr):
                return True
            if arr[index] != -1:
                return solve(index + 1, n, used, arr)

            for num in range(n,0, -1):
                if used[num]:
                    continue
                if num==1:
                    arr[index] = num
                    used[num] = True
                    if(solve(index+1, n, used, arr)):
                        return True
                    else:
                        arr[index] = -1
                        used[num] = False
                else:
                    if(index+num<len(arr) and arr[index+num]==-1):
                        arr[index] = num
                        arr[index+num] = num
                        used[num] = True
                        if (solve(index+1, n, used, arr)):
                            return True
                        else:
                            arr[index] = -1
                            arr[index+num] = -1
                            used[num] = False
            return False
        solve(0, n, used, arr)
        return arr
