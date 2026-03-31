class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        check = set()

        l, r, res = 0, 0, 0

        while r < len(s):

            if s[r] not in check: 

                res = max(res, r - l + 1)

                check.add(s[r])
                r += 1

            else: 
                while l <= r and s[r] in check:
                    check.remove(s[l])
                    l += 1
                

        return res



        



        