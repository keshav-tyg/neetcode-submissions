class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        place = {}

        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in place:
                return [place[difference], i]
            else:
                place[nums[i]] = i
        return []
        

        