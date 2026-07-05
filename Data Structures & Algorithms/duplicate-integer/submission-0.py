class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        without_duplicate=set(nums)
        if len(without_duplicate)==len(nums):
            return False
        else:
            return True
        