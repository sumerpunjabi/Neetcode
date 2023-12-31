# https://leetcode.com/problems/two-sum/description/

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        record = {}
        
        for i, x in enumerate(nums):
            difference = target - x
            if difference in record:
                return [record[difference], i]
            else:
                record[x] = i

        # since input is assumed to have only 1 solution this return is not required
        return []