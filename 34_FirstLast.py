class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans=[]
        n=len(nums)
        index=n//2
        while nums[index]!=target:
            if nums[index]==target:
                break
            elif nums[index]>target:
                index=(index+n)//2
            elif nums[index]<target:
                index=index//2
            else:
                ans=[-1,-1]

        while nums[index - 1] != target:
            index = index - 1
        ans.append(index)
        while nums[index + 1] != target:
            index = index + 1
        ans.append(index)
        return ans


