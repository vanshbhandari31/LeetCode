class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        lis=[]
        i=1
        if len(nums)==1:
            return False
        for i in range(len(nums)):
            if nums[i-1]==nums[i]:
                return True
            else:
                continue
        return False
