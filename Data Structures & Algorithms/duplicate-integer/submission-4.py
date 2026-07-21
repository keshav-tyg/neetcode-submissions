class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        bum = set()
        for i in nums:
            if i in bum:
                return True
            else:
                bum.add(i)
        return False