class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans=[]
        for i in range (len(s)):
            if s[i].isalpha():
                ans.append(s[i])
            elif not s[i].isalpha():
                if len(ans)!=0:
                    ans.pop()
                else:
                    continue
            else:
                continue
        ans="".join(ans)
        return ans