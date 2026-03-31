class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        hash = set(nums)
        lengths = [0]

        for num in nums: 
            largest = 0
            if (num -1 not in hash): 
                largest += 1
                while num + 1 in hash: 
                    largest += 1
                    num += 1
            lengths.append(largest)
        
        return max(lengths) 
                
            
                
        
        