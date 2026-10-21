class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        arr = set()
        for num in nums:
            if num not in arr:
                arr.add(num)
            else:
                return True
        return False
        