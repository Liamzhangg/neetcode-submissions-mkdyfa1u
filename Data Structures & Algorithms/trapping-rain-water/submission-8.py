class Solution:
    def trap(self, height: List[int]) -> int:

        area = 0
        l, r = 0, len(height)
        
        for i in range(1, len(height) - 1): 
            
            area += max(0, (min(max(height[l : i]), max(height[i+1 : r])) - height[i]))
        
        return area


        