class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        s = str(x)
        if s[0] == "-":
            s = s[-1:-(len(s)):-1]
            x = int(s)
            x = x * (-1)
            if x>((2**(31)) - 1) or x<(-2**(31)):
                return 0
            else:
                return x
        else:
            s = s[::-1]
            x = int(s)
            if x > ((2**(31)) - 1) or x < (-2**(31)):
                return 0
            else:
                return x
