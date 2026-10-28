from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)] 
        for key, v in c.items():
            buckets[v].append(key)
        res = []
        i = len(nums) - 1
        while len(res) != k:
            if buckets[i]:
                res.extend(buckets[i])
            i -= 1
        return res