class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        nGE = []
        ans = [0] * len(temperatures)
        for i in range(len(temperatures)):
            if not nGE:
                nGE.append(i)
            else:
                while nGE and temperatures[i] > temperatures[nGE[-1]]:
                    ind = nGE.pop()
                    ans[ind] = i - ind
                nGE.append(i)
        return ans
