class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            height = min(heights[l], heights[r])
            width = r - l
            area = height * width
            result = max(result, area)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        return result

                
