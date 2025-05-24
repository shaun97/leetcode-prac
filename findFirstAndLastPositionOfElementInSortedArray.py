class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        isFound = False
        mid = 0
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                isFound = True
                break
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        if not isFound:
            return [-1, -1]

        # check for left bound
        leftLeft, leftRight = left, mid
        leftIdx = 0

        while leftLeft <= leftRight:
            leftMid = leftLeft + (leftRight - leftLeft) // 2
            if nums[leftMid] == target:
                if leftMid == leftLeft or nums[leftMid - 1] < target:
                    leftIdx = leftMid
                    break
                else:
                    leftRight = leftMid - 1
            elif nums[leftMid] < target:
                leftLeft = leftMid + 1
            else:
                leftRight = leftMid - 1

        #check for right bound
        rightLeft, rightRight = mid, right
        rightIdx = 0
        while rightLeft <= rightRight:
            rightMid = rightLeft + (rightRight - rightLeft) // 2
            if nums[rightMid] == target:
                if rightMid == rightRight or nums[rightMid + 1] > target:
                    rightIdx = rightMid
                    break
                else:
                    rightLeft = rightMid + 1
            elif nums[rightMid] < target:
                rightLeft = rightMid + 1
            else:
                rightRight = rightMid - 1
        return [leftIdx, rightIdx]