class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""
        for i in s:
            if i.isalnum():
                cleaned +=  i.lower()

        left, right = 0, len(cleaned) - 1
        while left < right:
            if cleaned[left] != cleaned[right]:
                return False
            left += 1
            right -= 1
        return True