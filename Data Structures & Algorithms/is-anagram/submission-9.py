class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #the problem is sets dont contain duplicates
        # we have to use a list
        # but lists dont have O(1) lookup time

        if len(s) != len(t):
            return False
        seen = {}
        for char in range(len(s)):
            seen[s[char]] = seen.get(s[char], 0) + 1

        for char in range(len(t)):
            if t[char] not in seen or seen[t[char]] == 0:
                return False
            seen[t[char]] -= 1
        return True

        