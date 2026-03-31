class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        compare = {")" : "(", "}" : "{", "]" : "["}

        for char in s: 

            if char in compare: 
                if stack and stack[-1] == compare[char]:
                    stack.pop()
                else: 
                    return False

            else: 
                stack.append(char)

        return not stack