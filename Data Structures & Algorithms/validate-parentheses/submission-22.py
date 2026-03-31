class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        brackets ={")": "(", "}": "{", "]": "["}

        for item in s: 
            if item in brackets: 
                if stack and stack[-1] == brackets[item]: 
                    stack.pop(-1)
                else: 
                    return False

            else: 
                stack.append(item)

        return True if not stack else False
        

                



        