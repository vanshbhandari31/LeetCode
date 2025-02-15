class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=0
        s=s.rstrip()
        for i in range(len(s)):
            if s[i]==" ":
                l=0
            else:
                l=l+1
        return l


#THIS BELOW METHOD CAN ALSO BE USED:
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.strip().split()

        if not words:
            return 0

        return len(words[-1])


