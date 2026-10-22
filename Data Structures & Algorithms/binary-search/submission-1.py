class Solution:
    def search(self, nums: list[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while end >= start:
            index = start + int((end - start) / 2)
            num = nums[index]
            if num == target:
                return index
            elif target > num:
               start = index + 1
            else:
                end = index - 1
        return -1
