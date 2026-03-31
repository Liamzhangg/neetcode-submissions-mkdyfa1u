class Solution:

    def encode(self, strs: List[str]) -> str:

        str1 = ""
        for item in strs: 
            str1 += str(len(item)) + "#" + item
        
        return str1

    def decode(self, s: str) -> List[str]:

        strs, i = [], 0
        
        while i < len(s):
            j = i
            while s[j] != "#": 
                j += 1

            length = int(s[i:j])

            strs.append(s[j+1 : j + 1 + length])
            i = length + j + 1
        
        return strs




            

            

                

