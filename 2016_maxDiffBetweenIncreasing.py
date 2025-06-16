class Solution(object):
    def maximumDifference(self, nums):
        if len(nums) < 2:
            return -1

        min_val = nums[0]
        max_diff = -1

        for i in range(1, len(nums)):
            if nums[i] > min_val:
                max_diff = max(max_diff, nums[i] - min_val)
            else:
                min_val = nums[i]

        return max_diff
