class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[]
        answer=[]
        prod=1
        if nums.count(0)>=2:
            for i in range(len(nums)):
                answer.append(0)
            return answer
        elif nums.count(0)==1:
            ans=nums[:]
            ans.remove(0)
            for i in range(len(ans)):
                prod=prod*ans[i]
            for i in range(len(nums)):
                if  nums[i]!=0:
                    answer.append(0)
                else:
                    answer.append(prod)
            return answer
        else:
            for i in range(len(nums)):
                prod=prod*nums[i]
            for i in range(len(nums)):
                    product=prod/nums[i]
                    answer.append(product)
            return answer



