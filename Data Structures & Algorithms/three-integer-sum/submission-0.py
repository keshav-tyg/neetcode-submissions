class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # Costs O(n log n) but it will be O(n^2) anyways
        output = []
       
        #we have an anchor number
        # if the other 2 nums equal the negative of it, thats the set
        # we cycle through the loop with 1 number and finding the other 2 for it
        # with the 2 pointers

        

        for i in range(len(nums)):
            left, right = i + 1, len(nums) - 1
            target = -nums[i]
            #gets rid of duplicate anchors
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while left < right:
                current_sum = nums[left] + nums[right]
                #Triplet found, add it
                if current_sum == target:
                    output.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    #found triplet
                    #have a way to skip duplicates
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif current_sum < target:
                    left += 1
                else:
                    right -= 1


        return output



        
        