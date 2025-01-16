class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        output = 0

        n1 = len(nums1)
        n2 = len(nums2)


        output = 0


        if(n1%2):
            for num2 in nums2:
                output = output ^ num2

        if(n2%2):
            for num1 in nums1:
                output = output ^ num1

        return output