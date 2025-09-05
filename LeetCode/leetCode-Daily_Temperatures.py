class Solution:
    def dailyTemperatures(self, temperatures):
        stack = []
        answer = [0] * len(temperatures)
        for i, next_t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < next_t:
                idx = stack.pop()
                answer[idx] = i - idx
            stack.append(i)
        return answer

# temp = [73,74,75,71,69,72,76,73]
# print(Solution().dailyTemperatures(temp))