class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)%2!=0:
            return False
        dict={}
        for i in range(len(nums)):
            if nums[i] in dict.keys():
                cnt=dict.get(nums[i])+1
                dict[nums[i]]=cnt
            else:
                dict.update({nums[i]:1})
        check=dict.values()
        for i in range(len(check)):
            if check[i]%2!=0:
                return False
        return True


