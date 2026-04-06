class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        ans = -10000
        for i in range(len(nums)): 
            sum = 0
            for j in range(i, len(nums)): 
                sum += nums[j]
                ans = max(ans, sum)
        
        return ans



        