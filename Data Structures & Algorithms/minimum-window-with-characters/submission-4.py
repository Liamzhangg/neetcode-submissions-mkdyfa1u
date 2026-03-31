class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s): 
            return ""

        tCount = defaultdict(int)
        window = defaultdict(int)

        for char in t:
            tCount[char] += 1
        
        have, need = 0, len(tCount)

        res, resLen = [-1, -1], float("infinity")

        l = 0
        
        for r in range(len(s)): 
            char = s[r]
            window[char] += 1
            if char in tCount and window[char] == tCount[char]: 
                have += 1
            
            while have == need:

                if (r - l + 1) < resLen: 
                    res = [l,r]
                    resLen = (r - l + 1)
                
                window[s[l]] -= 1

                if s[l] in tCount and window[s[l]] < tCount[s[l]]: 
                    have -= 1
                
                l += 1

    
        l, r = res
        return s[l : r + 1]

                



        

        