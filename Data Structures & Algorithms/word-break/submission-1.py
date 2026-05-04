class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s)+1)
        dp[0] = True
        wordSet = set(wordDict)
        for i in range(1, len(s)+1):
            # if s[:i] in wordSet:
            #     dp[i] = True
            for j in range(i):
                dp[i] = dp[i] or (dp[j] and s[j:i] in wordSet)
                if dp[i]:
                    # optimization
                    break
        
        return dp[len(s)]