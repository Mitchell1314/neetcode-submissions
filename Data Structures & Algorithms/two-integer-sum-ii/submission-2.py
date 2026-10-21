class Solution:
    def twoSum(self, nums: list[int], target: int) ->list[int]:
        start_pointer = 0
        end_pointer = len(nums) - 1
        while end_pointer >= start_pointer:
            if nums[start_pointer] + nums[end_pointer] < target:
                start_pointer += 1
            elif nums[start_pointer] + nums[end_pointer] > target:
                end_pointer -= 1
            else:
                return [start_pointer+1, end_pointer+1]




        