# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # We can employ a binary search technique over here
        left = 1
        right = n
        mid = 1

        if isBadVersion(1):
            return 1

        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid + 1) and not isBadVersion(mid):
                return mid + 1
            # mid is bad, mid + 1 is bad
            elif isBadVersion(mid):
                right = mid
            # mid is not bad, mid + 1 is not bad
            else:
                left = mid + 1
        return mid
