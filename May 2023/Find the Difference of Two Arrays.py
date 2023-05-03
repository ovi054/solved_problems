class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        def binarySerach(x,nums):
            start = 0
            end = len(nums) - 1
            while(start<=end):
                mid = (start+end)//2
                if(x==nums[mid]):
                    return True
                elif(nums[mid]>x):
                    end = mid - 1
                else:
                    start = mid + 1
            return False
        output = []
        output.append([])
        for each in nums1:
            if(binarySerach(each,nums2)==False and binarySerach(each,output[0])==False):
                output[0].append(each)
        output.append([])
        for each in nums2:
            if(binarySerach(each,nums1)==False and binarySerach(each,output[1])==False):
                output[1].append(each)
        return output