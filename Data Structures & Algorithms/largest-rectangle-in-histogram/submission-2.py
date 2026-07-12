class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxVal = 0
        stack = []

        for i, n in enumerate(heights):
            start = i
            while stack and stack[-1][1] > n:
                index, num = stack.pop()
                maxVal = max(num * (i - index), maxVal)
                start = index
            stack.append((start, n))
        
        while stack:
            index, num = stack.pop()

            curr_max = (len(heights) - index) * num
            maxVal = max(curr_max, maxVal)
        
        return maxVal
        