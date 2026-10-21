class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort()
        visited = set()
        for i, num in enumerate(nums):
            if num  in visited:
                continue
            visited.add(num)
            target_sum = -num
            new_nums = nums[i+1:len(nums)]
            rst = self.twoSum(new_nums, target_sum)
            if len(rst) > 0:
                for r in rst:
                  r.append(num)
                  if r not in result:
                     result.append(r)
        return result
    def twoSum(self, nums, target):
        result = []
        start_pointer = 0
        end_pointer = len(nums) - 1
        while end_pointer > start_pointer:
            if nums[start_pointer] + nums[end_pointer] < target:
                start_pointer += 1
            elif nums[start_pointer] + nums[end_pointer] > target:
                end_pointer -= 1
            else:
                result.append([nums[start_pointer], nums[end_pointer]])
                start_pointer +=1

        return result