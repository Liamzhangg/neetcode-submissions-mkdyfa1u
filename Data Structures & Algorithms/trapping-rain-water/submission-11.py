class Solution:
    def trap(self, height: List[int]) -> int:
        # O(n^2)
        # area = 0
        # l, r = 0, len(height)
        
        # for i in range(1, len(height) - 1): 
            
        #     area += max(0, (min(max(height[l : i]), max(height[i+1 : r])) - height[i]))
        
        # return area

        area = 0
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]

        while l < r: 
            
            if leftMax > rightMax: 
                r -= 1
                rightMax = max(rightMax, height[r])
                area += rightMax - height[r]
            else:
                l += 1
                leftMax = max(leftMax, height[l])
                area += leftMax - height[l]
            

        return area



        