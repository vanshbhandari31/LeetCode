class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        uni = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                uni = uni + 1
                nums[uni] = nums[i]
                continue

        return uni + 1





