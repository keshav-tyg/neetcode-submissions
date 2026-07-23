class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        best = 0

        for right in range(len(s)):
            char = s[right]
            count[char] = count.get(char, 0) + 1

            max_frequency = max(count.values())

            while (right - left + 1) - max_frequency > k:
                count[s[left]] -= 1
                left += 1
                max_frequency = max(count.values())

            best = max(best, right - left + 1)

        return best