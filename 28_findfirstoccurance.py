class Solution(object):
    def strStr(self,haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        l1=len(haystack)
        l2=len(needle)
        i=0
        j=0
        counter=0
        while j<l1:

            if needle[i]==haystack[j]:
                i+=1
                j+=1
                if i==l2:
                    return j-i
                else:
                    continue
            else:
                counter += 1
                i=0
                j=counter
        return -1
