class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Brute force would be to iterate through all the sequences and check if they are correct O(2^2n * n)

        # Backtracking method
        # Adding an opening ot closing only if we know it is valid

        ans = []

        def backtrack(s=[], l=0, r=0):
            if len(s) == 2 * n:
                ans.append("".join(s))
                return
            if l < n:
                s.append("(")
                backtrack(s, l + 1, r)
                s.pop()
            if r < l:
                s.append(")")
                backtrack(s, l, r + 1)
                s.pop()

        backtrack()
        return ans
