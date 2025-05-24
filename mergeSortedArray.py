class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # fill up the array starting from the back of nums 1
        resItr = m + n - 1
        nums1Itr = m - 1
        nums2Itr = n - 1
        while nums1Itr >= 0 and nums2Itr >= 0:
            if nums1[nums1Itr] < nums2[nums2Itr]:
                nums1[resItr] = nums2[nums2Itr]
                resItr -= 1
                nums2Itr -= 1
            else:
                nums1[resItr] = nums1[nums1Itr]
                resItr -= 1
                nums1Itr -= 1
        if nums2Itr >= 0:
            for i in range(nums2Itr, -1, -1):
                nums1[i] = nums2[i]
