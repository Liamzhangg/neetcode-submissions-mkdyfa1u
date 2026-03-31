class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        ans = [0] * len(nums)

        if (nums.count(0) > 1): 
            return ans
        
        product = 1

        for num in nums: 
            if num != 0: 
                product *= num
        
        if nums.count(0) == 1: 
            for i in range(len(nums)): 
                if nums[i] == 0:
                    ans[i] = product
        
        else: 
            for i in range(len(nums)): 
                ans[i] = int(product / nums[i])
        
        return ans