class Solution(object):
    def getKey(self, word):
        count = [0] * 26
        for ch in word:
            count[ord(ch) - ord('a')] += 1
        return tuple(count)

    def groupAnagrams(self, strs):
        hash_map = {}

        for word in strs:
            key = self.getKey(word)
            if key not in hash_map:
                hash_map[key] = []
            hash_map[key].append(word)

        return list(hash_map.values())
