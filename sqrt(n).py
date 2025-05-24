class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        left = 2
        right = x // 2

        while right >= left:
            mid = left + (right - left) // 2
            mid_squared = mid * mid
            if mid_squared == x:
                return int(mid)
            elif mid_squared > x:
                right = mid - 1
            else:
                left = mid + 1

        return int(right)
