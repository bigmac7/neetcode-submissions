class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j, num in enumerate(nums, start=i+1):
                if j > len(nums) -1:
                    break
                if nums[i] + nums[j] == target:
                    return [i, j]

        