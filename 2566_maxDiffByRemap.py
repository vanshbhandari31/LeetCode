class Solution(object):
    def minMaxDifference(self, num):
        """
        :type num: int
        :rtype: int
        """
        newnum=str(num)
        numMax=''
        numMin=''
        replaceMax='inf'
        replaceMin='inf'
        for i in newnum:
            if i!='9':
                replaceMax=i
                break

        if replaceMax !='inf':
            for i in newnum:
                if i==replaceMax:
                    numMax=numMax+'9'
                else:
                    numMax = numMax + i
        else:
            numMax=str(num)


        for i in newnum:
            if i!='0':
                replaceMin=i
                break
        if replaceMin!='inf':
            for i in newnum:
                if i==replaceMin:
                    numMin=numMin+'0'
                else:
                    numMin = numMin + i
        else:
            numMin=str(num)

        return int(numMax)-int(numMin)
