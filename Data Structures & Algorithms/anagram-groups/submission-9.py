class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = defaultdict(list)        
        
        for item in strs:
            count = [0]*26 

            for char in item: 
                count[ord(char) - ord("a")] += 1
            
            hash[tuple(count)].append(item)
        
        return list(hash.values())

  