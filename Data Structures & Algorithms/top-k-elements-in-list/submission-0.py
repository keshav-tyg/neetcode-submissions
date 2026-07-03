class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # We need a counter
        # the numbers that are seen the most are going to be returned, and how many of them
        # There are
        # if the numbers are tied, return both

        seen = {}
        for i in nums:
            seen[i] = seen.get(i, 0) + 1
        sorted_data = sorted(seen.items(), key=lambda item: item[1])
        #we need colon after k to get the tuple
        return [pair[0] for pair in sorted_data[-k:]]
