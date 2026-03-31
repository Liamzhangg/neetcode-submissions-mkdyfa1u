class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        brackets = {")": "(", "]": "[", "}": "{"}
        for item in s: 
            if item in brackets:
                if stack and stack[-1] == brackets[item]: 
                    stack.pop() #pops last item in list
                else: 
                    return False
            
            else: 
                stack.append(item)
        
        return True if not stack else False





        