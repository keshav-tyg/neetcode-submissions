class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = [] #stack where we can add and pop stuff, # gets added in the order and should be removed in the order
        pairs = { ")": "(", "]": "[", "}": "{" } # if the closer is in pairs, its value should be there too

        for char in s:
            if char in pairs: # it is a closer
                if not stack or stack[-1] != pairs[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)

        return len(stack) == 0