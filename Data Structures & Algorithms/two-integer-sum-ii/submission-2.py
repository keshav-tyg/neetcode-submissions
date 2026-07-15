class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        output = []
        left, right = 0, len(numbers) - 1
        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                output = [left + 1, right + 1]
                return output
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        return output


        