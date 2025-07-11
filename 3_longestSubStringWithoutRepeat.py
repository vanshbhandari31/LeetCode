class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left=0
        longest=0
        curr=set()
        for right in range(0,len(s)):
            while s[right] in curr:
                curr.remove(s[left])
                left += 1
            curr.add(s[right])
            newM=len(curr)
            longest=max(longest,newM)
        return longest

