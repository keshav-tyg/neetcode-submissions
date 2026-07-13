class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # make the list a set
        # because with set the lookup times with 
        # "is in" will become O(1)

        numset = set(nums)
        longest = 0

        #we will make it so we will check if n - 1 exists, if it does then we are in the middle of the chain
        # if it doesnt then we will see if n + 1 exists, if it does then we will keep going
        # if it doesnt then the longest chain length is 1

        for num in numset:
            if num - 1 not in numset:
                current = num
                length = 1

                while current + 1 in numset:
                    current += 1
                    length += 1
                longest = max(longest, length)
        return longest
                


                        



        