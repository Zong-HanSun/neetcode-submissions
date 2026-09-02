class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area_seen = 0

        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                height = min(heights[i], heights[j])
                width = j - i
                current_area = height * width
                
                if current_area > max_area_seen:
                    max_area_seen = current_area

        return max_area_seen
        