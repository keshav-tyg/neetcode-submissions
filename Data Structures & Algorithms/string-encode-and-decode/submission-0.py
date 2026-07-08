class Solution:

    def encode(self, strs: List[str]) -> str:
        #combine strings into one and then decoder removes strings agaim
        pieces = []
        for i in strs:
           pieces.append(str(len(i)) + "#" + i)
        return "".join(pieces)

    def decode(self, s: str) -> List[str]:

        strings = []
        #start i from 0
        i = 0
        # While i is smaller than the length of the string
        while i < len(s):
            #returns the index value of where # is 
            j = s.index("#", i)
            #find the length of the string
            length = int(s[i:j])
            #gets the string j+1 (because we are ignoring the # to the length of the string)
            string = s[j+1: j+1+length]
            #append the string into list
            strings.append(string)
            #move i past the string
            i = j + 1 + length


        return strings

           
            


            

