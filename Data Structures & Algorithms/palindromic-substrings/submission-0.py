class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[False] * len(s) for _ in range(len(s))]

        res = 0
        for i in range(len(s)):
            dp[i][i] = True
            res+=1
        n = len(s)
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    # If length is 2 (j-i == 1), it's a palindrome
                    # If length > 2, check if inner part is a palindrome
                    if j - i == 1 or dp[i+1][j-1]:
                        dp[i][j] = True
                        res += 1
        return res