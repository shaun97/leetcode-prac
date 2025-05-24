class Solution:
    def minSwaps(self, data: List[int]) -> int:
        numberOfOnes = 0
        for num in data:
            if num == 1:
                numberOfOnes += 1

        if numberOfOnes == 1:
            return 0

        first, second = 0, 0
        minNumberOfZero = 0
        currNumberOfZero = 0

        while second < numberOfOnes:
            if data[second] == 0:
                minNumberOfZero += 1
            second += 1

        currNumberOfZero = minNumberOfZero

        while second < len(data):
            if data[first] == 0:
                currNumberOfZero -= 1
            if data[second] == 0:
                currNumberOfZero += 1
            second += 1
            first += 1
            minNumberOfZero = min(minNumberOfZero, currNumberOfZero)

        return minNumberOfZero
