class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0
        hash = set()
        ans = 0

        for r in range(len(s)): 

            while s[r] in hash: 
                hash.remove(s[l]) 
                l += 1
            
            hash.add(s[r])

            ans = max(ans, (r - l) + 1)

        return ans

