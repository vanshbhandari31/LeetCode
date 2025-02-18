class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        ans=[0]*len(temperatures)
        stack=[]
        for i in range(len(temperatures)-1,-1,-1):
            if not stack:
                stack.append(i)
                ans[i]=0
            while stack and temperatures[i]>=temperatures[stack[-1]]:
                stack.pop()
            if not stack:
                ans[i]=0
            else:
                ans[i]=stack[-1]-i
            stack.append(i)
        return ans


