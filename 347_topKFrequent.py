import heapq


class Solution(object):
    import heapq
    def topKFrequent(self,nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dict1={}
        for i in range(len(nums)):
            if nums[i] in dict1.keys():
                x=dict1[nums[i]]+1
                dict1.update({nums[i]:x})
            else:
                dict1[nums[i]]=1
        heap=[(-value,key)for key,value in dict1.items()]
        print(heap)
        heapq.heapify(heap)
        print(heap)
        i=0
        l=[]
        while i<k:
            value,key=heapq.heappop(heap)
            heapq.heapify(heap)
            l.append(int(key))
            i=i+1
        return l








