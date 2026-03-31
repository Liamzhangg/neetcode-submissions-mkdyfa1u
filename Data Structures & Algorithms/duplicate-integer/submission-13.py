class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        hashmap = {}
        for item in nums: 
            if item in hashmap: 
                return True
            hashmap[item] = True

        return False
        
        
