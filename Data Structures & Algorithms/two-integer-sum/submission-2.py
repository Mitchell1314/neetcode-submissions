class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        for index, num in enumerate(nums):
               remaining = target - num
               if remaining in hashmap:
                return [hashmap[remaining], index]

               hashmap[num] = index
        return []


        