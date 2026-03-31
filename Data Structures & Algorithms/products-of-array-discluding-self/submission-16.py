class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # O(n) time and O(1) space

        ans = [1] * len(nums)

        prefix = 1

        for i in range(len(nums)): 
            ans[i] = prefix
            prefix *= nums[i]
        
        suffix = 1

        for i in range(len(nums) - 1, -1, -1): 
            ans[i] *= suffix
            suffix *= nums[i]

        return ans


        # ANSWER IN O(n) using division
    
        # ans = [0] * len(nums)

        # zero_count = nums.count(0)
        # if (zero_count > 1): 
        #     return ans
        
        # product = 1

        # for num in nums: 
        #     if num != 0: 
        #         product *= num
        
        # if zero_count == 1: 
        #     for i in range(len(nums)): 
        #         if nums[i] == 0:
        #             ans[i] = product
        
        # else: 
        #     for i in range(len(nums)): 
        #         ans[i] = int(product / nums[i])
        
        # return ans