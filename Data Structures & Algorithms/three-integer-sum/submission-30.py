class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        ans = []

        nums.sort()

        # if len(nums) == 3: 
        #     if (sum(nums) == 0): 
        #         ans.append(nums)
        
        for i, item in enumerate(nums): 

            if (item == nums[i-1] and i > 0): 
                continue

            left, right = i + 1, len(nums) - 1

            while (left < right): 

                sum = item + nums[left] + nums[right]

                if (sum == 0): 
                    ans.append([item, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while (nums[left] == nums[left-1] and left < right): 
                        left += 1
    
                if (sum > 0): 
                    right -= 1
                if (sum < 0): 
                    left += 1
                
    
                
                

                    
        return ans



        