class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Use a monotonic stack.
        stack = [-1]
        ans = max(heights)
        for idx, val in enumerate(heights):
            while stack[-1] != -1 and heights[stack[-1]] >= val:
                # Do the magic here
                current_height = heights[stack.pop()]
                ans = max(ans, (idx-stack[-1]-1)*current_height)
            stack.append(idx)
        while stack[-1] != -1:
            current_height = heights[stack.pop()]
            current_width = len(heights) - stack[-1] - 1
            ans = max(ans, current_height * current_width)
        return ans

