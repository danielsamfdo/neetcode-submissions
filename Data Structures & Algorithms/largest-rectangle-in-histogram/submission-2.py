class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        ans = 0
        # Add a 0 to the end to flush out all remaining bars in the stack
        heights.append(0)
        
        for idx, val in enumerate(heights):
            while stack[-1] != -1 and heights[stack[-1]] >= val:
                current_height = heights[stack.pop()]
                # Width is current index - new top of stack - 1
                width = idx - stack[-1] - 1
                ans = max(ans, current_height * width)
            stack.append(idx)
            
        # Clean up the 0 we added if you're worried about modifying input
        heights.pop() 
        return ans

