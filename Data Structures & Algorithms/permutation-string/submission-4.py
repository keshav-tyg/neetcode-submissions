class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False    # window can't fit
        
        # Count chars in s1
        s1_count = {}
        for char in s1:
            s1_count[char] = s1_count.get(char, 0) + 1
        
        # Sliding window of size len(s1) over s2
        window_count = {}
        window_size = len(s1)
        
        # Build initial window (first len(s1) chars of s2)
        for i in range(window_size):
            char = s2[i]
            window_count[char] = window_count.get(char, 0) + 1
        
        # Check if initial window matches
        if window_count == s1_count:
            return True
        
        # Slide window forward one char at a time
        for i in range(window_size, len(s2)):
            # Add new char on the right
            char_in = s2[i]
            window_count[char_in] = window_count.get(char_in, 0) + 1
            
            # Remove old char on the left
            char_out = s2[i - window_size]
            window_count[char_out] -= 1
            if window_count[char_out] == 0:
                del window_count[char_out]     # clean up for equality check
            
            # Check if match
            if window_count == s1_count:
                return True
        
        return False