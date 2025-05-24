class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missingNumberIterator = 0

        for num in arr:
            missingNumberIterator += 1
            while missingNumberIterator != num:
                k -= 1
                if k == 0:
                    return missingNumberIterator
                missingNumberIterator += 1

        while k > 0:
            missingNumberIterator += 1
            k -= 1

        return missingNumberIterator

    def findKthPositiveBinarySearch(self, arr: List[int], k: int) -> int:
        # the number of missing elements at a given index is number at index - index - 1
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = left + (right - left) // 2
            midK = arr[mid] - 1 - mid

            if midK < k:
                left = mid + 1
            else:
                right = mid - 1

        return left + k
