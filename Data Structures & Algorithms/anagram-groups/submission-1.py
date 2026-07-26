class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Dictionary to store anagram groups, keyed by sorted characters
        anagram_map = {}
        
        # Iterate through each string
        for s in strs:
            # Sort the characters in the string to create a canonical key
            sorted_s = ''.join(sorted(s))
            
            # Add the original string to the group for this sorted key
            if sorted_s not in anagram_map:
                anagram_map[sorted_s] = []
            anagram_map[sorted_s].append(s)
        
        # Return all groups as a list of lists
        return list(anagram_map.values())