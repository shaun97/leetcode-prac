import heapq
from typing import List
class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        # push all into pqueue
        # use a diff array to keep track of subequent
        queries.sort(key=lambda x: x[0])
        diff_arr = [0] * (len(nums) + 1)
        offset = 0
        removal = 0
        queryPtr = 0
        pQ = [] # store all those eligible 
        for i in range(len(nums)):
            for j in range(queryPtr, len(queries)):
                if queries[j][0] <= i:
                    heapq.heappush(pQ, (-queries[j][1]))
                    queryPtr += 1
                else:
                    break
            offset += diff_arr[i]
            nums[i] -= offset
            while pQ and nums[i] > 0:
                endQuery = -heapq.heappop(pQ)
                if endQuery < i:
                    removal += 1
                    continue
            offset += 1
            diff_arr[endQuery + 1] -= 1
            nums[i] -= 1
            if nums[i] > 0:
                return -1
        return len(pQ) + removal