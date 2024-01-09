# https://leetcode.com/problems/group-anagrams/

from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:   

        words = defaultdict(list)

        for i in strs:
            sort = ''.join(sorted(i))
            words[sort].append(i)

        return list(words.values())
