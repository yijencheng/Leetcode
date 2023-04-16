# Idea: 
# 
# Better
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [(temperatures[0], 0)]
        ans = [0]* len(temperatures)
        for i in range(1, len(temperatures)):
            cur = temperatures[i] 
            while stack and stack[-1][0] < cur:
                _, idx = stack.pop()
                ans[idx] = i-idx
            stack.append((cur, i))
        return ans

# takeaway: 先確認pop的情境、最後再append。
# correct
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [(temperatures[0], 0)]
        ans = [0]* len(temperatures)
        for i in range(1, len(temperatures)):
            cur = temperatures[i] 
            if not stack or cur <= stack[-1][0]:
                stack.append((cur, i))
            else:
                while stack and stack[-1][0] < cur:
                    _, idx = stack.pop()
                    ans[idx] = i-idx
                stack.append((cur, i))
        return ans

# wrong, index out of range  and forget to append
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [(temperatures[0], 0)]
        ans = [0]* len(temperatures)
        for i in range(1, len(temperatures)):
            cur = temperatures[i] 
            if cur <= stack[-1][0]:
                stack.append((cur, i))
            else:
                while stack[-1][0] < cur:
                    _, idx = stack.pop()
                    ans[idx] = i-idx
        return ans