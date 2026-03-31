class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        ans = 0
        l = 0
        hash = defaultdict(int)

        for r in range(len(s)): 

            hash[s[r]] += 1

            while (r - l + 1) - max(hash.values()) > k: 
                hash[s[l]] -= 1
                l += 1


            ans = max(ans, r - l + 1)

        return ans
                    