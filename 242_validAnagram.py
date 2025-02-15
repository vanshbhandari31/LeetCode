class Solution(object):
    def isAnagram(self,s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ls1=list(s)
        ls2=list(t)
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            if ls2[i] in ls1:
                ls1.remove(ls2[i])
            else:
                return False
        if len(ls1)==0:
            return True
        else:
            return False


