class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        countR = 0
        countW = 0
        countB = 0
        for i in range(len(nums)):
            if nums[i]==0:
                countR+=1
            elif nums[i]==1:
                countW+=1
            else:
                countB+=1

        idx=0
        for i in range(countR):
            nums[idx]=0
            idx+=1
        for i in range(countW):
            nums[idx]=1
            idx+=1
        for i in range(countB):
            nums[idx]=2
            idx+=1
        return nums




