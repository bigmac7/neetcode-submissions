class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        res = []
        for num in nums:
            prod *= num
        for i, num in enumerate(nums):
            if num == 0:
                new_prod = 1
                nums.remove(0)
                for num in nums:
                    new_prod *= num
                res.append(int(new_prod))
                nums.insert(i, 0)
                continue
            else:
                res.append(int(prod / num))
            
        return res