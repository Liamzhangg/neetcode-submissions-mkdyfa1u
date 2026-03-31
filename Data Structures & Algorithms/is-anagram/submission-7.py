class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        hashmap1 = defaultdict(int)
        hashmap2 = defaultdict(int)
        for i in range(len(s)): 
            hashmap1[s[i]] += 1
        for i in range(len(t)): 
            hashmap2[t[i]] += 1

        if (hashmap1 == hashmap2):
            return True
        
        return False



        