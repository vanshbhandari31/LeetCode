class Solution(object):
    def isPalindrome(self,s):
        """
        :type s: str
        :rtype: bool
        """
        ns=""

        for char in s :
            if char.isalnum():
                ns=ns+char
        ns=ns.lower()
        rs=ns[::-1]
        if ns==rs:
            return True
        else:
            return False


