class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # for each recursive step, for each number between the starting number and n, we pick one and do a recursive call.
        # i.e [1, 2, 3, 4] -> we pick 1 and call the function for [2, 3, 4], we pick 2 and call the function for [3, 4].
        # in the base case, we stop calling when n - i (the number we are calling) is less than k. Meaning that the remaining numbers are not enough to copmlete

        def combineR(starting: int, n: int, remaining_k: int):
            res = []
            for i in range(starting, n + 1):
                if remaining_k == 1:
                    res.append([i])
                elif n - i >= remaining_k - 1:
                    res += [[i] +
                            sublist for sublist in combineR(i + 1, n, remaining_k - 1)]
            return res

        return combineR(1, n, k)

    def combineS(self, n: int, k: int) -> List[List[int]]:
        def backtrack(first=1, curr=[]):
            # if the combination is done
            if len(curr) == k:
                output.append(curr[:])
            for i in range(first, n + 1):
                # add i into the current combination
                curr.append(i)
                # use next integers to complete the combination
                backtrack(i + 1, curr)
                # backtrack
                curr.pop()

        output = []
        backtrack()
        return output
