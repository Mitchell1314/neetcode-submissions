class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = []
        result.append(1)
        suffix = 1
        for index in range(0, len(nums)):
            if index >= 1:
               result.append(result[index-1] * nums[index - 1])
        for j in range(len(nums)-1,-1,-1):
            if j < len(nums)-1:
                suffix = suffix * nums[j+1]
                result[j] = suffix * result[j]
        return result