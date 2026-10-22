class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        result = [0 for i in range(0, len(temperatures))]
        for i, temperature in enumerate(temperatures):
           if i == 0:
               stack.append(i)
           else:
               while stack and temperatures[stack[-1]] < temperature:
                   index = stack.pop()
                   result[index] = i - index
               stack.append(i)
        return result
        



        

        