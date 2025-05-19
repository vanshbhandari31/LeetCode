class Solution(object):
    def isanagram(self,s1,s2):
        if len(s1)!=len(s2):
            return False
        count1=[0]*26
        count2=[0]*26
        for i in s1:
            count1[ord(i)-ord('a')]+=1
        for i in s2:
            count2[ord(i)-ord('a')]+=1
        return count1==count2

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res=[]
        visited=[False]*len(strs)
        for i in range(len(strs)):
            if not visited[i]:
                group=[strs[i]]
                visited[i]=True

                for j in range(i+1,len(strs)):
                    if not visited[j] and self.isanagram(strs[i],strs[j]):
                        group.append(strs[j])
                        visited[j]=True
                res.append(group)
        return res


