class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #find the 2 pairs with the largest area
        # the index value = bottom length
        # min(value1,value2) * distance = largest area

       

        
        output = 0
        left, right = 0, len(heights) - 1
        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            area  = width * height
            output = max(output, area)
            
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return output



        


    
    
        