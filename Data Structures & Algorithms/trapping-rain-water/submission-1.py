class Solution:
    def trap(self, height: List[int]) -> int:
        lMax = [0] * len(height)
        rMax = [0] * len(height)
        lMax[0] = height[0]
        rMax[len(height)-1] = height[len(height)-1]
        for i in range(1, len(height)):
            lMax[i] = max(lMax[i-1], height[i])

        for i in range(len(height) - 2, -1, -1):
            rMax[i] = max(rMax[i+1],height[i])
        res = 0
        for i in range(len(height)):
            res += min(lMax[i], rMax[i]) - height[i]
        return res