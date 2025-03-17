class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        finans=[]
        for i in range(len(nums)):
            ans=[]
            visited=[]
            
