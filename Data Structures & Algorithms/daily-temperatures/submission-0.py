class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # brute force approach
        res = [0]*(len(temperatures))

        for i in range(len(temperatures)):
            val = temperatures[i]
            for j in range(i+1,len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    res[i] = j - i
                    break
            

        return res