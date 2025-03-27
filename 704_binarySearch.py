class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        mid=len(nums)//2
        if target==nums[mid]:
            return mid
        elif target<nums[mid]:
            return self.search(nums[:mid],target)
        elif target>nums[mid]:
             res= self.search(nums[mid+1:],target)
             if res!=-1:
                 return mid+res+1
             else:
                 return -1
