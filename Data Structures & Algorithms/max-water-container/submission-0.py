class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, (len(heights) - 1)

        curr_max = 0

        while l < r:
            height = heights[l] if heights[l] < heights[r] else heights[r]
            distance = r - l
            volume = height * distance

            curr_max = max(curr_max, volume)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return curr_max