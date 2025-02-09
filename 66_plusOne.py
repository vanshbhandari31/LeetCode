class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s=""
        for i in range(len(digits)):
            s=s+str(digits[i])
        num=int(s)
        num+=1
        s=str(num)
        lst=[]
        for i in range(len(s)):
            lst.append(int(s[i]))
        return lst