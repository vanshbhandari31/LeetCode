class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        answer = []
        for i in range(len(temperatures)):
            answer.append(0)
        n = len(temperatures)
        for i in range(n):
            curr = temperatures.pop(0)
            newn=len(temperatures)
            j = 0
            while j < newn:
                if temperatures[j] > curr:
                    answer[i] = answer[i] + j+1
                    break
                j = j + 1

        return answer


