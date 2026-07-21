class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        bum = set()
        for i in range(len(nums)):
            if nums[i] in bum:
                return True
            else:
                bum.add(nums[i])
        return False