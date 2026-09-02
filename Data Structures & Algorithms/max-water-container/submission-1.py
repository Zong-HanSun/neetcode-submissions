class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area_seen = 0

        left = 0
        right = len(heights) - 1

        while left < right:
            height = min(heights[left], heights[right])
            width = right - left
            current_area = height * width

            if current_area > max_area_seen:
                max_area_seen = current_area

            if heights[left] <= heights[right]:
                left+=1
                
            elif heights[right] < heights[left]:
                right-=1
        
        return max_area_seen