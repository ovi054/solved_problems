class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lessList = []
        equalList = []
        GreaterList = []

        for num in nums:
            if num<pivot:
                lessList.append(num)
            elif num==pivot:
                equalList.append(num)
            else:
                GreaterList.append(num)

        return lessList+equalList+GreaterList