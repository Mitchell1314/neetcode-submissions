class Solution:
    def maxArea(self, heights: list[int]) -> int:
        start = 0
        end = len(heights) - 1
        max_area = end * min(heights[start], heights[end])
        while end > start:
            if heights[start] <= heights[end]:
                start += 1
            else:
                end -= 1
            area = (end-start)*min(heights[start], heights[end])
            max_area = max(area, max_area)
        return max_area
        