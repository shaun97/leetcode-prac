class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        # With k = 2, we can form any permutation -> we bring the letter we want to shift to the front
        # We use the the position 1 to bring all other letters to the back
        # therefore, if k > 2, the answer is just to sort the list 

        if k == 1:
            return min(s[i:] + s[:i] for i in range(len(s)))
        else:
            return "".join(sorted(s))