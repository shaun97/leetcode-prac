class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # increase the length of the subsequence by 1 until you encounter
        # a repeat character, increment the start by 1 until there are no repeating characters
        # use two pointers to signify the start and end of the substring
        curr_substr = longest_substr = 0
        length = len(s)
        lhs = rhs = 0
        hash_of_curr_substr = {}
        while rhs < length:
            curr_substr += 1
            curr_char = s[rhs]
            while curr_char in hash_of_curr_substr:
                lhs_char = s[lhs]
                del hash_of_curr_substr[lhs_char]
                curr_substr -= 1
                lhs += 1

            hash_of_curr_substr[curr_char] = 1
            longest_substr = max(longest_substr, curr_substr)
            rhs += 1
        return longest_substr
