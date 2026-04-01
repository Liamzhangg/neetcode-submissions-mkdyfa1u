class Solution:

    def encode(self, strs: List[str]) -> str:
        
        str1 = ""

        for item in strs: 
            str1 += str(len(item)) + "*" + item 
        
        return str1

    def decode(self, s: str) -> List[str]: 

        i = 0 
        ans = []

        while i < len(s): 

            j = i

            while s[j] != "*": 
                j += 1
            
            length = int(s[i:j])

            ans.append(s[j + 1: j + 1 + length])

            i = j + 1 + length
        
        return ans



            

            

                

