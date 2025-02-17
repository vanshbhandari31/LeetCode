from itertools import combinations
from math import factorial


class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        from itertools import permutations
        ans = []
        # n=len(tiles)-len(set(tiles))

        for i in range(len(tiles) + 1):
            perms = permutations(tiles, i)
            for j in perms:
                ans.append(j)
        ans = set(ans)
        return len(ans) - 1
