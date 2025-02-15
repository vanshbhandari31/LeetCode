class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        val = 0
        tdict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        while i in range(len(s) - 1):
            if s[i] in ['I'] and s[i + 1] in ['V', 'X']:
                val = val + tdict.get(s[i + 1]) - tdict.get(s[i])
                i = i + 2
            elif s[i] in ['X'] and s[i + 1] in ['C', 'L']:
                val = val + tdict.get(s[i + 1]) - tdict.get(s[i])
                i = i + 2
            elif s[i] in ['C'] and s[i + 1] in ['D', 'M']:
                val = val + tdict.get(s[i + 1]) - tdict.get(s[i])
                i = i + 2
            else:
                val = val + tdict.get(s[i])
                i = i + 1
        if i != len(s):
            val = val + tdict.get(s[-1])
            return val
        else:
            return val
