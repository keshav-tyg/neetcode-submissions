class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #The nums have to multiply each other
        #Ex 6 * 4 * 2 * 1
        # 6 * 2 * 1
        # there has to be no duplicates, so i guess a set would work
        # The output cant be an element of nums
        output = []
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if i != j:
                    product *= nums[j]
            output.append(product)
        return output


        