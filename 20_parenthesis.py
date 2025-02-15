class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        check=[]
        for i in range (len(s)):
            if s[i] in (")","]","}") and (len(check)==0):
                return False
            if s[i] in ("(","{","["):
                check.append(s[i])
            elif s[i]==")":
                    if (len(check)==0) or  check[-1]!="(":
                        return False
                    else:
                        check.pop()
            elif s[i]=="}":
                    if (len(check)==0) or  check[-1]!="{":
                        return False
                    else:
                        check.pop()
            elif s[i]=="]":
                    if (len(check)==0) or  check[-1]!="[":
                        return False
                    else:
                        check.pop()
        if len(check)==0:
            return True
        else:
            return  False
