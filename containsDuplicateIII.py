class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        counter = {}
        for idx, num in enumerate(nums):
            if counter.get(num):
                counter[num].append(idx)
            else:
                counter[num] = [idx]

        for key, item in counter.items():
            if len(item) > 1:
                for i in range(0, len(item) - 1):
                    if abs(item[i] - item[i + 1]) <= k:
                        return True

        return False
