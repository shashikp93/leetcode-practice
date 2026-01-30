
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_idx = {}

        for i, j in enumerate(nums):
            if target - j in val_idx:
                return [i, val_idx[target - j]]

            val_idx[j] = i
