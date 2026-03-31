class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hash = defaultdict(int)
        ans = [0]*k

        for i in range(len(nums)):
            hash[nums[i]] += 1
        
        index = list(hash.keys())
        
        for i in range(k): 
            max_val = max(hash.values())
            for key, value in hash.items(): 
                if (value == max_val):
                    max_key = key 
                    break
                    
            ans[i] = max_key
            hash.pop(key)
        
        return ans
            


        