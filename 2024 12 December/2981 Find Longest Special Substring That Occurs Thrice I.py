class Solution:
    def maximumLength(self, s: str) -> int:

        n = len(s)
        def isPossible(value):
            countList = [0]*26
            count = 1
            char = s[0]
            index = ord(s[0])-ord('a')
            if(count>=value):
                countList[index]+=1
            if(countList[index]>=3):
                return True
            for i in range(1, n):
                index = ord(s[i])-ord('a')
                if(char==s[i]):
                    count+=1
                    if(count>=value):
                        countList[index]+=1
                    if(countList[index]>=3):
                        return True
                else:
                    count = 1
                    char = s[i]
                    if(count>=value):
                        countList[index]+=1
                    if(countList[index]>=3):
                        return True
            return False


        start = 1
        end = len(s)
        output = -1

        while(start<=end):
            mid =  (start+end)//2
            print(mid)
            if(isPossible(mid)):
                output= max(output, mid)
                start = mid + 1
            else:
                end = mid - 1
        
        return output