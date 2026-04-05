class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        check = set()

        l, r, ans = 0, 0, 0

        if len(s) == 1: 
            return 1

        while r < len(s): 

            if s[r] not in check:  
                ans = max(ans, r - l + 1)
                check.add(s[r])
                r += 1

            
            else: #s[r] is already in check

                while s[r] in check: 
                    check.remove(s[l]) 
                    l += 1
            
        return ans



        



        