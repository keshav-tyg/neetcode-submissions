class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        letters = set()
        max_count = 0

        for right, char in enumerate(s):
            
            while char in letters:
                letters.remove(s[left])
                left += 1
            letters.add(char)

            max_count = max(max_count, right - left + 1)
        return max_count

        