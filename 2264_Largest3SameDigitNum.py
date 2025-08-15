class Solution(object):
    def largestGoodInteger(self, num):
        curr = ""
        x = len(num)
        for i in range(x - 2):
            if num[i] == num[i+1] == num[i+2]:
                triple = num[i:i+3]
                if curr == "" or triple > curr:
                    curr = triple
        return curr
