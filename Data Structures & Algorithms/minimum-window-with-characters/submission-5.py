from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s: return ""

        countT = Counter(t)
        window = {}
        
        # 'need' is the number of UNIQUE characters in T
        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("inf")
        l = 0
        
        for r, char in enumerate(s):
            window[char] = 1 + window.get(char, 0)

            # Check if this character just completed its requirement
            if char in countT and window[char] == countT[char]:
                have += 1

            while have == need:
                # Update result if this window is smaller
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                # Shrink from the left
                left_char = s[l]
                window[left_char] -= 1
                # If removing this char breaks the requirement, decrement 'have'
                if left_char in countT and window[left_char] < countT[left_char]:
                    have -= 1
                l += 1
                
        l, r = res
        return s[l : r + 1] if resLen != float("inf") else ""