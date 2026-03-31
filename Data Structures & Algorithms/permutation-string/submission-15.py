class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len (s2): 
            return False 
        
        s1Count = [0] * 26
        s2Count = [0] * 26

        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        l, r = 1, len(s1)

        if s2Count == s1Count: return True


        while r < len(s2): 

            s2Count[ord(s2[l - 1]) - ord('a')] -= 1
            s2Count[ord(s2[r]) - ord('a')] += 1
            l += 1
            r += 1  
            if (s2Count == s1Count): return True

    
         

        return False      