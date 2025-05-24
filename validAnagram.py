class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap_s = {}
        hashmap_j = {}
        for i in s:
            if i in hashmap_s:
                hashmap_s[i] += 1
            else:
                hashmap_s[i] = 1

        for i in t:
            if i in hashmap_j:
                hashmap_j[i] += 1
            else:
                hashmap_j[i] = 1

        if hashmap_s == hashmap_j:
            return True
        else:
            return False
