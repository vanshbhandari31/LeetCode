class Solution(object):
    def maximum69Number(self, num):
        """
        :type num: int
        :rtype: int
        """
        x=str(num)
        for i in range(len(x)):
            if x[i]=="6":
                x=x.replace("6", "9", 1)
                return int(x)
        return num
