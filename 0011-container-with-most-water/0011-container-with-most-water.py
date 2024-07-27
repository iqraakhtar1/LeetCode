class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        result = 0
        while left < right:
            water = (right - left) * min(height[left], height[right])
            if water > result:
                result = water
            if height[left] < height[right]:
                left+=1
            else:
                right-=1
        return result
        