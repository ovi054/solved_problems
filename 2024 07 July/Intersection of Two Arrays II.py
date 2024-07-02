class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        i,j=0,0
        m,n = len(nums1),len(nums2)
        while i<m and j<n:
            if(nums1[i]==nums2[j]):
                output.append(nums1[i])
                i+=1
                j+=1
            elif(nums1[i]<nums2[j]):
                i+=1
            else:
                j+=1
        return output
        