class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums) == 0:
          return 0
        nums.sort()
        max_len = 0
        current_len = 1
        for i in range(1, len(nums)):
              if nums[i] - nums[i-1] == 1:
                current_len += 1
              elif nums[i] - nums[i-1] < 1:
                  continue
              else:
                  max_len = max(max_len, current_len)
                  current_len = 1
        max_len = max(max_len, current_len)
        return max_len
               
