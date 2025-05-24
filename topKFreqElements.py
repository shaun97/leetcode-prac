from queue import PriorityQueue


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            if counter.get(num):
                counter[num] += 1
            else:
                counter[num] = 1

        minq = PriorityQueue()
        for key, count in counter.items():
            minq.put((count, key))
            if minq.qsize() > k:
                minq.get()

        res = []
        while minq.qsize() > 0:
            res.append(minq.get()[1])

        return res

    def topKFrequentQS(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums

        counter = {}

        for num in nums:
            if counter.get(num):
                counter[num] += 1
            else:
                counter[num] = 1

        unique = list(counter.keys())

        def partition(left, right, pivot_index) -> int:
            pivot_freq = counter[unique[pivot_index]]
            # move the pivot number to the end
            temp = unique[pivot_index]
            unique[pivot_index] = unique[right]
            unique[right] = temp

            store_index = left
            for i in range(left, right):
                if counter[unique[i]] < pivot_freq:
                    temp = unique[store_index]
                    unique[store_index] = unique[i]
                    unique[i] = temp
                    store_index += 1

            temp = unique[right]
            unique[right] = unique[store_index]
            unique[store_index] = temp

            return store_index

        def quickselect(left, right, k_smallest):
            if left == right:
                return

            pivot_index = random.randint(left, right)
            pivot_index = partition(left, right, pivot_index)

            if k_smallest == pivot_index:
                return
            elif k_smallest < pivot_index:
                quickselect(left, pivot_index - 1, k_smallest)
            else:
                quickselect(pivot_index + 1, right, k_smallest)

        n = len(unique)
        quickselect(0, n - 1, n - k)
        return unique[n - k:]
