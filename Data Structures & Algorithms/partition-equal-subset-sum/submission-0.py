class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2
        # dp[i] will be True if a sum of i is possible
        dp = [False] * (target + 1)
        dp[0] = True
        
        for num in nums:
            # Iterate backwards to ensure we don't use the same 
            # element multiple times for the same target sum.
            for i in range(target, num - 1, -1):
                if dp[i - num]:
                    dp[i] = True
            
            # Early exit if we found the target
            if dp[target]:
                return True
                
        return dp[target]