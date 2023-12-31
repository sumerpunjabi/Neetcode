# https://leetcode.com/problems/group-anagrams/

from typing import List
from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:   

        words = dict()

        for i in strs:
            count = Counter(i)
            sort = ''.join(sorted(count.elements()))
            if sort in words:
                words[sort].append(i)
            else:
                words[sort] = [i]

        return [list(v) for v in words.values()]
