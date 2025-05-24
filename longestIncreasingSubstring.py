import bisect


class Solution:
    def lengthOfLISDP(self, nums: List[int]) -> int:
        dp = (len(nums)) * [1]

        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

    def lengthOfLISAlt(self, nums: List[int]) -> int:
        # greedy algorithm. The best way of building a subsequence is to iterate through every element and for each element
        # if it is larger than the max of our subsequence, we add it to the subsequence
        # if it is not, then replace the first element that is greater than or eqaul to the element with the element.
        res = [nums[0]]
        for num in nums:
            if num > max(res):
                res.append(num)
            else:
                for r in res:
                    if r >= num:
                        res.remove(r)
                        res.append(num)

        return len(res) - 1

    def lengthOfLISAltWBinarySearch(self, nums: List[int]) -> int:
        sub = []
        for num in nums:
            i = bisect.bisect_left(sub, num)

            # If num is greater than any element in sub
            if i == len(sub):
                sub.append(num)

            # Otherwise, replace the first element in sub greater than or equal to num
            else:
                sub[i] = num

        return len(sub)
