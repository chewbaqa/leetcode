# hmap that stores the value and index of prev nums, compares by takin difference of target and current value and checkin for the diff in hmap
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prev:
                return [prev[diff], i]
            prev[n] = i
        return 0
