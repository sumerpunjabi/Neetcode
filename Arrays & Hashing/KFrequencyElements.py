# https://leetcode.com/problems/top-k-frequent-elements/

from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        return [num for num, freq in count.most_common(k)]
