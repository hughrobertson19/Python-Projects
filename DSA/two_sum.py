try:
    from typing import List  # ✅ Works in modern Python versions
except ImportError:
    List = list  # ✅ Fallback for older versions of Python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        return []