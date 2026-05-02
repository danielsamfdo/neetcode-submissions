from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s: return ""

        dict_t = Counter(t)
        required = len(dict_t) # Number of UNIQUE chars in t
        
        window_counts = {}
        formed = 0 # Number of unique chars in window that meet dict_t freq
        
        # ans: (window length, left, right)
        ans = float("inf"), None, None
        l = 0

        for r in range(len(s)):
            char = s[r]
            window_counts[char] = window_counts.get(char, 0) + 1

            # Only increment 'formed' when the count of a specific char 
            # matches its required count in dict_t exactly.
            if char in dict_t and window_counts[char] == dict_t[char]:
                formed += 1

            # Shrink the window from the left until it's no longer 'valid'
            while l <= r and formed == required:
                char = s[l]

                # Update the smallest window found so far
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                window_counts[char] -= 1
                # If removing this char breaks the "required" condition
                if char in dict_t and window_counts[char] < dict_t[char]:
                    formed -= 1
                
                l += 1    

        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]
