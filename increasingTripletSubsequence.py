class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # we keep track of 2 arrays -> one with the ongoing lowest element and the other with 2 elements formed
        # if the lowest one finds another element that is larger than it, but this element is smaller than the
        # second array, this array will replace the larger one
        if len(nums) < 3:
            return False

        lowestElement = nums[0]
        onGoingArray = [nums[0]]

        for num in nums:
            if num < lowestElement:
                lowestElement = num

            if num > onGoingArray[-1]:
                if len(onGoingArray) == 2:
                    return True
                else:
                    onGoingArray.append(num)
            elif num < onGoingArray[-1]:
                if len(onGoingArray) == 1:
                    onGoingArray[0] = num
                elif num > onGoingArray[0]:
                    onGoingArray[1] = num
                else:
                    if num > lowestElement:
                        onGoingArray[0] = lowestElement
                        onGoingArray[1] = num

        return False
