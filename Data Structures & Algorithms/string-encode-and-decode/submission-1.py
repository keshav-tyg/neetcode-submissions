class Solution:

    def encode(self, strs: List[str]) -> str:
        #encode a list of strings to one string
        #have a foramt where first its the number of letters per string, then
        # then the '#' to know when to stop, then the string
        # ex 5#monkey#5donkey
        pieces = []
        for i in strs:
            #return str because the whole thing is a string
            pieces.append(str(len(i))+ "#" + i)
        return "".join(pieces)

    def decode(self, s: str) -> List[str]:
        #have a loop that runs until we reach the end of the string
        strings = []
        i = 0
        while i < len(s):
            #find index of #
            j = s.index("#", i)
            length = int(s[i:j])    
            strings.append(s[j+1 : j+1+length])
            #update i
            i = 1 + j + length
        return strings



